# -*- coding: utf-8 -*-
### VERSION 2.00 STANDALONE
### TESTED ON WINDOWS PYTHON 3.8.2

import logging
import re
from os import path

from tqdm import tqdm

import mik

logger = logging.getLogger(__name__)


class ReadCadastralFile:

    def __init__(self, data):

        self.Header = HeaderLayer(data)
        self.CadasterLayer = CadasterLayer(data, self.Header)
        self.CadasterControl = ControlCadastre(data)
        def controlCheck(cl, cc):
            if (len(cl.lineObj) == cc.lines) and (len(cl.contourObj) == cc.contours) and (
                    len(cl.symbolObj) == cc.symb) and (len(cl.gepointObj) == cc.points) and (len(cl.textObj) == cc.txt):
                return "PASS"
            else:
                return "FAIL"

        self.CHECK = controlCheck(self.CadasterLayer, self.CadasterControl)
        self.Buildings = Buildings(data, self.Header)

    def __getitem__(self, item):
        return getattr(self, item)


class HeaderLayer:

    def __init__(self, data):
        rx_header = re.compile(
            "HEADER\s*VERSION\s+(\S+)\s*EKATTE\s+(.*)\s*NAME\s+(.*)\s*PROGRAM\s+(\S+)\s+V?(\S+)\s*DATE\s+(.*)\s*FIRM\s+(.*)\s*REFERENCE\s+(\S+)\s+(\S+)\s*WINDOW\s+(.*)\s*COORDTYPE\s+(\d+),(.*)\s*CONTENTS\s+(.*)\s*COMMENT\s+(.*)\s*END_HEADER",
            re.MULTILINE)
        extract = rx_header.search(data).groups()

        self.cadversion = extract[0].replace("\r", "")
        self.ekatte = extract[1].replace("\r", "")
        self.loc = extract[2].replace("\r", "")
        self.sw = extract[3].replace("\r", "")
        self.swv = extract[4].replace("\r", "")
        self.date = extract[5].replace("\r", "")
        self.firm = extract[6].replace("\r", "")

        self.refX = float(extract[8].replace("\r", ""))
        self.refY = float(extract[7].replace("\r", ""))
        self.window = extract[9].replace("\r", "")
        self.coordid = extract[10].replace("\r", "")
        self.coordidh = extract[11].replace("\r", "")
        self.content = extract[12].replace("\r", "")
        self.comments = extract[13].replace("\r", "")

    def __getitem__(self, item):
        return getattr(self, item)


def objectSearch(data):
    rx_textobj = re.compile(
        "^T\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s(\S+)\s+(\S+)\s+(\S+)\s+[LCR][TCD]\s+(?:(?:\"(.*)\"\s)?[CPLVSA]\s+(\S+)\s(AN|SI|NU|LE|XC|YC|HI|AR|LP|AD|ST|IO)\s)?\"(.*)\"",
        re.MULTILINE)
    rx_lineobj = re.compile(
        "(?:^L\s+(\d+)\s+(\d+)\s+(\d+)\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))\s+)((?:(?:\S+)\s+(?:\S+)\s+(?:\S+)\s+(?:\S+)\s+(?:\S+)\s+(?:\S+);(?:\s+)?)*)",
        re.MULTILINE)
    rx_conobj = re.compile(
        "C\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))\s+((?:(?:\d+)\s+)*)",
        re.MULTILINE)
    rx_symbobj = re.compile(
        "S\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))",
        re.MULTILINE)
    rx_geopointobj = re.compile(
        "P\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(?:(\d+(?:.\d+)*)|(?:0))\s+(?:(\d+(?:.\d+)*)|(?:0))\s+(\d+)\s+(?:(\d+(?:.\d+)*)|(?:0))\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+\"(.*)\"\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))",
        re.MULTILINE)
    lineObjectsStrings = rx_lineobj.finditer(data)
    contObjectsStrings = rx_conobj.finditer(data)
    geoPtObjectsStrings = rx_geopointobj.finditer(data)
    textObjectsStrings = rx_textobj.finditer(data)
    symbObjectsStrings = rx_symbobj.finditer(data)
    return lineObjectsStrings, contObjectsStrings, geoPtObjectsStrings, textObjectsStrings, symbObjectsStrings


class CadasterLayer:
    def __init__(self, data, hdr):

        rx_cadLayer = re.compile("LAYER CADASTER([\s\S]*?)END_LAYER")
        extract = rx_cadLayer.search(data).group()
        parse = objectSearch(extract)

        if parse[0]:
            self.lineObj = [LineC(line.groups(), hdr) for line in parse[0]]
        if parse[1]:
            self.contourObj = [ContC(contour.groups(), hdr) for contour in parse[1]]
        if parse[2]:
            self.gepointObj = [GeoPointC(geopt.groups(), hdr) for geopt in parse[2]]
        if parse[3]:
            self.textObj = [TextC(text.groups(), hdr) for text in parse[3]]
        if parse[4]:
            self.symbolObj = [SymbolC(symb.groups(), hdr) for symb in parse[4]]


    def __getitem__(self, item):
        return getattr(self, item)


class ControlCadastre:
    def __init__(self, data):
        rx_controlCadaster = re.compile("CONTROL CADASTER([\S\s]*)END_CONTROL")

        extract = rx_controlCadaster.search(data).group()

        self.points = int(re.search(r"(?:NUMBER_POINTS\s+(\d+)\s+)", extract).group(1))
        self.lines = int(re.search(r"(?:NUMBER_LINES\s+(\d+)\s+)", extract).group(1))
        self.symb = int(re.search(r"(?:NUMBER_SYMBOLS\s+(\d+)\s+)", extract).group(1))
        self.txt = int(re.search(r"(?:NUMBER_TEXTS\s+(\d+)\s+)", extract).group(1))
        self.contours = int(re.search(r"(?:NUMBER_CONTURS\s+(\d+)\s+)", extract).group(1))

    def __getitem__(self, item):
        return getattr(self, item)


class Buildings:
    def __init__(self, data, hdr):

        rx_LevelSchemasLayer = re.compile("LAYER SHEMI([\s\S]*?)END_LAYER")
        rx_Levels = re.compile("ET\s+(\S+)\s+(\S+)\s+([\s\S]*?)END_ET")
        extract = rx_Levels.finditer(rx_LevelSchemasLayer.search(data).group(0))
        self.list = []
        if extract:
            for et in extract:
                if not (et.group(1) in [bid.id for bid in self.list]):
                    b = Building(et.group(1))
                    b.addLevel(et.groups(), hdr)
                    self.list.append(b)
                else:
                    self.list[[bid.id for bid in self.list].index(et.group(1))].addLevel(et.groups(),
                                                                                         hdr)

    def __getitem__(self, item):
        return getattr(self, item)


class Building:
    def __init__(self, uid):
        self.id = uid
        self.levels = []

    def addLevel(self, lvldata, hdr):
        l = LevelObj(lvldata, hdr)
        self.levels.append(l)

    def __getitem__(self, item):
        return getattr(self, item)


class LevelObj:
    def __init__(self, data, hdr):
        self.lvl = data[1]
        parse = objectSearch(data[2])

        if parse[0]:
            self.lineObj = [LineC(line.groups(), hdr) for line in parse[0]]
        if parse[1]:
            self.contourObj = [ContC(contour.groups(), hdr) for contour in parse[1]]

    def __getitem__(self, item):
        return getattr(self, item)


class LineC:
    def __init__(self, array, hdr):
        self.type = str(array[0])
        self.lid = int(array[1])
        self.bordertype = str(array[2])
        self.datecreated = str(array[3])
        self.datedestroyed = str(array[4])
        rx_ptlist = re.compile("(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+);")
        self.ptlist = [LinecPt(p.groups(), hdr) for p in rx_ptlist.finditer(array[5])]
        self.get_point_sequence = [pt.get_XY for pt in self.ptlist]
        self.get_referenced_point_sequence = [pt.get_XYR for pt in self.ptlist]

    def __getitem__(self, item):
        return getattr(self, item)


class LinecPt:
    def __init__(self, array, hdr):
        self.ptN = int(array[0])
        self.ptY = float(array[1])
        self.ptX = float(array[2])
        self.ptacc = array[3]
        self.permasig = array[4]
        self.deter = array[5]
        self.get_XY = self.ptX, self.ptY
        self.get_XYR = self.ptX + hdr.refX, self.ptY + hdr.refY
        self.ptXR = self.ptX + hdr.refX
        self.ptYR = self.ptY + hdr.refY

    def __getitem__(self, item):
        return getattr(self, item)


class ContC:
    def __init__(self, array, hdr):
        self.type = array[0]
        self.cid = array[1]
        self.posY = float(array[2])
        self.posX = float(array[3])
        self.datecreated = array[4]
        self.datedestroyed = array[5]
        rx_contid = re.compile("(\d+)")
        self.ids = rx_contid.findall(array[6])
        self.posXR = self.posX + hdr.refX
        self.posYR = self.posY + hdr.refY

    def __getitem__(self, item):
        return getattr(self, item)

class TextC:
    def __init__(self, array, hdr):
        self.type = int(array[0])
        self.id = int(array[1])
        self.posY = float(array[2])
        self.posX = float(array[3])
        self.posXR = self.posX + hdr.refX
        self.posYR = self.posY + hdr.refY

        self.posH = float(array[4])
        self.datecreated = array[5]
        self.datedestroyed = array[6]
        self.rotgon = float(array[7])
        self.rotdeg = (100 - float(array[7])) * 180.0 / 200.0
        self.halign = str(array[8])
        self.valign = str(array[9])

        self.prefixtext = str(array[10])

        self.objtype = str(array[11])
        self.graphicid = str(array[12])
        self.grapicparam = str(array[13])

        self.suffixtext = str(array[14])

    def __getitem__(self, item):
        return getattr(self, item)


class GeoPointC:
    def __init__(self, array, hdr):
        self.type = array[0]
        self.id = array[1]
        self.posY = float(array[2])
        self.posX = float(array[3])
        self.posH = float(array[4])
        self.posclass = array[5]
        self.accy = array[6]
        self.accx = array[7]
        self.hclass = array[8]
        self.acch = array[9]
        self.stab = array[10]
        self.stabalt = array[11]
        self.nsig = array[12]
        self.underg = array[13]
        self.oldN = array[14]
        self.datecreated = array[15]
        self.datedestroyed = array[16]
        self.posXR = self.posX + hdr.refX
        self.posYR = self.posY + hdr.refY

    def __getitem__(self, item):
        return getattr(self, item)

class SymbolC:
    def __init__(self, array, hdr):
        self.type = array[0]
        self.id = array[1]
        self.posY = float(array[2])
        self.posX = float(array[3])
        self.rot = array[4]
        self.scale = array[5]
        self.datecreated = array[6]
        self.datedestroyed = array[7]
        self.posXR = self.posX + hdr.refX
        self.posYR = self.posY + hdr.refY

    def __getitem__(self, item):
        return getattr(self, item)

def opener(filename):
    if path.exists(filename[:-4] + "_cached.tcad"):
        filename = filename[:-4] + "_cached.tcad"
    f = open(filename, "rb")
    filetext = f.read()
    try:
        cadText = filetext.decode("utf-8")
    except:
        cadText = translate(filetext).replace("\r", "")
        ff = open(filename[:-4] + "_cached.tcad", "x", encoding="utf-8")
        ff.write(cadText)
        ff.close()
    return cadText


def translate(textbytes):
    goodText = ""
    print("TRANSLATION IN PROGRESS")
    for i in tqdm(range(len(textbytes))):
        if ((textbytes[i] >= 128) and (textbytes[i] <= 191)):
            letter = str(mik.mikdict.get(textbytes[i]))
        else:
            letter = chr(textbytes[i])
        goodText = goodText + letter

    return goodText
