import copy

import ezdxf
from ezdxf import zoom
from ezdxf.tools.standards import linetypes  # some predefined linetypes

import config
import layerstemplate


def drawBuildingHatch(object, doc, ms):
    layer = layerManager(doc, "hatch")
    for pgon in object.CadasterLayer.contourObj:
        try:
            if not (pgon.pgon_bad_flag):
                if pgon.type == 1:
                    if pgon.pgon_pt is not None:
                        hatch = ms.add_hatch(color=256, dxfattribs={"layer": layer})
                        hatch.paths.add_polyline_path(pgon.pgon_pt, is_closed=1)
        except Exception as e:
            print(e)
            continue


def drawLines(line, doc, ms, layerAlreadyCreated=None):
    for i in range(len(line)):
        try:
            current = line[i]
            if layerAlreadyCreated is not None:
                layer = layerAlreadyCreated
            else:
                layer = layerManager(doc, current.type)
            ms.add_lwpolyline(current.get_referenced_point_sequence, dxfattribs={"layer": layer})
        except Exception as e:
            print(e)
            continue


def drawText(object, doc, ms):
    # get all texts
    txtObjs = object.CadasterLayer.textObj
    layer = layerManager(doc, "txt")

    for i in range(len(txtObjs)):
        try:
            current = txtObjs[i]
            txt = "{prefix}{suffix}".format(prefix=current.prefixtext.replace("None", ""),
                                            suffix=current.suffixtext.replace("None", ""))
            cleantxt = txt.replace("\\", "").replace("\n", "").replace("\r", "").replace("\"", "")
            ms.add_text(cleantxt, dxfattribs={"layer": layer, 'style': 'custom', 'height': 1.0,
                                              'rotation': current.rotdeg}).set_pos((current.posXR, current.posYR),
                                                                                   align='LEFT')
        except Exception as e:
            print(e)
            continue


def drawContours(contourObj, doc, ms, layerAlreadyCreated=None):
    if layerAlreadyCreated is not None:
        layer = layerAlreadyCreated
    else:
        layer = layerManager(doc, "cid")

    for i in range(len(contourObj)):
        try:
            current = contourObj[i]
            ms.add_text(current.cid, dxfattribs={"layer": layer, 'style': 'custom', 'height': 1.0}).set_pos(
                (current.posXR, current.posYR), align='LEFT')
        except Exception as e:
            print(e)
            continue


class geopt_block:
    def __init__(self, dwg):
        # Create a block with the name 'FLAG'
        geopt = dwg.blocks.new(name='geopt')
        # geopt.add_polyline2d([(0, 0), (0, 5), (4, 3), (0, 3)])
        geopt.add_circle((0, 0), .15, dxfattribs={'color': 2})
        geopt.add_lwpolyline([(-.3, 0), (.3, 0)], dxfattribs={'color': 2})
        geopt.add_lwpolyline([(0, -.3), (0, .3)], dxfattribs={'color': 2})
        geopt.add_circle((0, 0), .2, dxfattribs={'color': 3})

    def insert(self, modelspace, l, point, xscale, yscale, rot):
        modelspace.add_blockref("geopt", point, dxfattribs={'xscale': xscale, 'yscale': yscale, 'rotation': rot})


def geoptdraw(object, doc, ms):
    geoptObj = object.CadasterLayer.gepointObj
    layer = layerManager(doc, "gp")

    blk = geopt_block(doc)
    for geopoint in geoptObj:
        try:
            blk.insert(ms, layer, (geopoint.posXR, geopoint.posYR), 1.0, 1.0, 0.0)
            ms.add_text(str(geopoint.id),
                        dxfattribs={"layer": layer, 'style': 'custom', 'height': 0.2, 'rotation': 0.0}).set_pos(
                (geopoint.posXR, geopoint.posYR), align='LEFT')
        except Exception as e:
            print(e)
            continue


def layerManager(doc, layerid, so=None):
    if so is None:
        layerprops = layerstemplate.clt.get(layerid)
    else:
        layerprops = copy.copy(layerstemplate.clt.get("so"))
        layerprops[0] = "{0} {1}".format(layerprops[0], so)
    if layerprops[0] not in doc.layers:
        doc.layers.new(name=layerprops[0],
                       dxfattribs={'linetype': layerprops[1], 'lineweight': layerprops[2], 'color': layerprops[3]})
    return layerprops[0]


def schemadraw(buildings, doc, ms):
    for currentBuilding in buildings:
        for currentLevel in currentBuilding.levels:
            lineLayerName = layerManager(doc, 190, currentLevel.lvl)
            drawLines(currentLevel.lineObj, doc, ms, lineLayerName)

            contourLayerName = layerManager(doc, 190, "{0} txt".format(currentLevel.lvl))
            drawContours(currentLevel.contourObj, doc, ms, contourLayerName)

    for l in doc.layers:
        if layerstemplate.clt.get("so")[0] in l.dxf.name:
            l.off()


def makedxf(object):
    outputPathDXF = "{path}{fname}.dxf".format(path=config.PATHS_CONFIG['dirOutput'], fname=object.Filename)

    doc = ezdxf.new(dxfversion='AC1015')
    doc.styles.new('custom', dxfattribs={'font': 'arial.ttf', 'width': 1})
    for name, desc, pattern in linetypes():
        if name not in doc.linetypes:
            doc.linetypes.new(name=name, dxfattribs={'description': desc, 'pattern': pattern})
    modelspace = doc.modelspace()

    if len(object.CadasterLayer.contourObj) > 0: drawBuildingHatch(object, doc, modelspace)
    if len(object.CadasterLayer.lineObj) > 0: drawLines(object.CadasterLayer.lineObj, doc, modelspace)
    if len(object.CadasterLayer.contourObj) > 0: drawContours(object.CadasterLayer.contourObj, doc, modelspace)
    if len(object.CadasterLayer.textObj) > 0: drawText(object, doc, modelspace)
    if len(object.CadasterLayer.gepointObj) > 0: geoptdraw(object, doc, modelspace)

    if len(object.Buildings.list) > 0:
        schemadraw(object.Buildings.list, doc, modelspace)
    zoom.extents(modelspace)
    doc.saveas("test.dxf")
