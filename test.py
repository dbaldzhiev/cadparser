import os

import matplotlib as plt

import cadutils


def tests():
    dir = "./testdata"
    testfiles = []
    for file in os.listdir(dir):
        if file.endswith(".cad"):
            # print(os.path.join(".\\testdata", file))
            testfiles.append(os.path.join(dir, file))

    CF = []
    for t in testfiles:
        try:
            CF.append(cadutils.ReadCadastralFile(cadutils.opener(t)))
        except Exception:
            pass

    for i in range(len(CF)):
        # print("File {0} Cadaster {1} and Tables {2}".format(testfiles[i],CF[i].CADASTERCHECK[0],CF[i].CADASTERCHECK[1]))
        if CF[i].CADASTERCHECK != "Fail":
            print(f"{testfiles[i]:<30} CADASTRE {CF[i].CADASTERCHECK[0]:>2} | TABLES {CF[i].CADASTERCHECK[1]:>2}")
        else:
            print(f"{testfiles[i]:<30} COMPLETE FAILURE")
    return CF


def pl(data):
    for con in data.CadasterLayer.contourObj:
        try:
            plt.ion()
            plt.figure()
            plt.suptitle(con.cid, fontsize=16)

            # print(con.pgon_ext)
            plt.plot([x[0] for x in con.pgon_ext], [y[1] for y in con.pgon_ext])

            if len(con.pgon_holes) > 0:
                # plt.figure()
                # plt.plot([x[0] for x in con.pgon_ext], [y[1] for y in con.pgon_ext])
                for hole in con.pgon_holes:
                    plt.plot([x[0] for x in hole], [y[1] for y in hole])
            # plt.show()

        except Exception:
            pass

    try:
        plt.show()
    except Exception:
        pass


def plsec(data):
    con = data.CadasterLayer.contourObj[9]
    plt.figure()
    plt.suptitle(con.cid, fontsize=16)
    plt.plot([x[0] for x in con.pgon_ext], [y[1] for y in con.pgon_ext])
    if len(con.pgon_holes) > 0:
        plt.figure()
        plt.plot([x[0] for x in con.pgon_ext], [y[1] for y in con.pgon_ext])
        for hole in con.pgon_holes:
            plt.plot([x[0] for x in hole], [y[1] for y in hole])
    plt.show()
