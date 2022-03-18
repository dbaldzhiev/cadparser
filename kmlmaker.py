# VERSION 3.00
import simplekml
from pyproj import Transformer

import config

transformer = Transformer.from_crs(config.BGS2005, config.WGS84, always_xy=True)


def gpsCoords(pts):
    return [transformer.transform(x, y) for x, y in pts]


def makekml(object):
    kml = simplekml.Kml()
    for polylgon in object.CadasterLayer.contourObj:
        kmlpgon = kml.newpolygon(name=polylgon.cid)
        kmlpgon.outerboundaryis = gpsCoords(polylgon.pgon_pt)
        if int(polylgon.type) == 1:
            kmlpgon.style.polystyle.color = simplekml.Color.changealphaint(100, simplekml.Color.blue)
        elif int(polylgon.type) == 2:
            kmlpgon.style.polystyle.color = simplekml.Color.changealphaint(60, simplekml.Color.red)
        else:
            kmlpgon.style.polystyle.color = simplekml.Color.changealphaint(30, '99ffac59')
    kml.save("{path}{fname}.kml".format(path=config.PATHS_CONFIG['dirOutputKML'], fname=object.Filename))
