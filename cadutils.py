# -*- coding: utf-8 -*-
### VERSION 2.00 STANDALONE
### TESTED ON WINDOWS PYTHON 3.8.2

import datetime
import logging
import re
import sys
from datetime import datetime
from os import path

from tqdm import tqdm

import mik

logger = logging.getLogger(__name__)


class ReadCadastralFile:
    def __init__(self, data):
        self.Header = HeaderLayer(data)
        self.CadasterLayer = CadasterLayer(data, self.Header)

    def __getitem__(self, item):
        return getattr(self, item)


class HeaderLayer:

    def __init__(self, data):
        rx_header = re.compile(
            "HEADER\s*VERSION\s+(\S+)\s*EKATTE\s+(.*)\s*NAME\s+(.*)\s*PROGRAM\s+(\S+)\s+V?(\S+)\s*DATE\s+(.*)\s*FIRM\s+(.*)\s*REFERENCE\s+(\S+)\s+(\S+)\s*WINDOW\s+(.*)\s*COORDTYPE\s+(\d+),(.*)\s*CONTENTS\s+(.*)\s*COMMENT\s+(.*)\s*END_HEADER",
            re.MULTILINE)
        extractedHeader = rx_header.search(data)
        a = extractedHeader.groups()

        self.cadversion = a[0].replace("\r", "")
        self.ekatte = a[1].replace("\r", "")
        self.loc = a[2].replace("\r", "")
        self.sw = a[3].replace("\r", "")
        self.swv = a[4].replace("\r", "")
        self.date = a[5].replace("\r", "")
        self.firm = a[6].replace("\r", "")

        self.refX = float(a[8].replace("\r", ""))
        self.refY = float(a[7].replace("\r", ""))
        self.window = a[9].replace("\r", "")
        self.coordid = a[10].replace("\r", "")
        self.coordidh = a[11].replace("\r", "")
        self.content = a[12].replace("\r", "")
        self.comments = a[13].replace("\r", "")

    def __getitem__(self, item):
        return getattr(self, item)


class CadasterLayer:
    def __init__(self, data, hdr):

        rx_LCadaster = re.compile("LAYER CADASTER([\s\S]*?)END_LAYER")
        cadItem = rx_LCadaster.search(data).group()
        rx_textobj = re.compile(
            "^T\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s(\S+)\s+(\S+)\s+(\S+)\s+(L|C|R)(T|C|D)\s+(?:(?:\"(.*)\"\s)?(C|P|L|V|S|A)\s+(\S+)\s(AN|SI|NU|LE|XC|YC|HI|AR|LP|AD|ST|IO)\s)?\"(.*)\"",
            re.MULTILINE)
        rx_lineobj = re.compile(
            "(^L\s+(\d+)\s+(\d+)\s+(\d+)\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))\n)((?:(?:\S+)\s+(?:\S+)\s+(?:\S+)\s+(?:\S+)\s+(?:\S+)\s+(?:\S+);(?:\s+)?)*)",
            re.MULTILINE)
        rx_conobj = re.compile("C\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))\n((?:(?:\d+)\s+)*)", re.MULTILINE)
        rx_symbobj = re.compile("S\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))", re.MULTILINE)
        rx_geopointobj = re.compile(
            "P\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(?:(\d+(?:.\d+)*)|(?:0))\s+(?:(\d+(?:.\d+)*)|(?:0))\s+(\d+)\s+(?:(\d+(?:.\d+)*)|(?:0))\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+\"(.*)\"\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))\s+((?:\d{1,2}\.\d{1,2}\.\d{2,4})|(?:0))",
            re.MULTILINE)


        textObjectsStrings = rx_textobj.finditer(cadItem)
        lineObjectsStrings = rx_lineobj.finditer(cadItem)

        contObjectsStrings = rx_conobj.finditer(cadItem)
        symbObjectsStrings = rx_symbobj.finditer(cadItem)

        geoPtObjectsStrings = rx_geopointobj.finditer(cadItem)

        if lineObjectsStrings:
            print("PARSING LINES:")
            self.lineObj = [LineC(line.groups(), hdr) for line in lineObjectsStrings]
        if contObjectsStrings:
            print("PARSING CONTOURS:")
            self.contourObj = [ContC(contour.groups(), hdr) for contour in contObjectsStrings]

        if textObjectsStrings:
            self.textObj = [TextC(text.groups(), hdr) for text in textObjectsStrings]

        if symbObjectsStrings:
            print("PARSING SYMBOLS:")
            self.symbolObj = [SymbolC(symb.groups(), hdr) for symb in symbObjectsStrings]
        if geoPtObjectsStrings:
            print("PARSING GEOPOINTS:")
            self.gepointObj = [GeoPointC(geopt.groups(), hdr) for geopt in geoPtObjectsStrings]

    def __getitem__(self, item):
        return getattr(self, item)


class LineC:
    def __init__(self, array, hdr):
        self.type = str(array[1])
        self.lid = int(array[2])
        self.bordertype = str(array[3])
        self.datecreated = str(array[4])
        self.datedestroyed = str(array[5])
        rx_ptlist = re.compile("(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+);")
        self.ptlist = [LinecPt(p.groups(),hdr) for p in rx_ptlist.finditer(array[6])]
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


class SchemaLevelC:
    def __init__(self, array, hdr):
        self.level = array[0][1]
        self.id = array[0][0]
        self.storeyLines = []
        for line in array[1]:
            self.storeyLines.append(LineC(line))
        self.storeyContours = []
        for contour in array[2]:
            self.storeyContours.append(ContC(contour))

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


class SymbolC:
    def __init__(self, array,hdr):
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