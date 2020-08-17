import os

import cadutils


def tests():
    dir = ".\\testdata\\source"
    testfiles = []
    for file in os.listdir(dir):
        if file.endswith(".cad"):
            # print(os.path.join(".\\testdata", file))
            testfiles.append(os.path.join(dir, file))

    CF = []
    for t in testfiles:
        CF.append(cadutils.ReadCadastralFile(cadutils.opener(t)))

    for i in range(len(CF)):
        # print("File {0} Cadaster {1} and Tables {2}".format(testfiles[i],CF[i].CADASTERCHECK[0],CF[i].CADASTERCHECK[1]))
        if CF[i].CADASTERCHECK != "Fail":
            print(f"{testfiles[i]:<30} CADASTRE {CF[i].CADASTERCHECK[0]:>2} | TABLES {CF[i].CADASTERCHECK[1]:>2}")
        else:
            print(f"{testfiles[i]:<30} COMPLETE FAILURE")
    return CF
