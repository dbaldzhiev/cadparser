# VERSION 3.00
import sys

import cadutils
import config
import dxfmaker
import kmlmaker

if __name__ == '__main__':
    filename = sys.argv[1]

    cadobject = cadutils.ReadCadastralFile(filename)
    dxfmaker.makedxf(cadobject)
    kmlmaker.makekml(cadobject)

    if config.debug:
        try:
            from matplotlib import pyplot as plt

            plt.figure()
            for c in cadobject.CadasterLayer.contourObj:
                plt.suptitle(c.cid, fontsize=16)
                if c.pgon_pt:
                    plt.plot([x[0] for x in c.pgon_pt], [y[1] for y in c.pgon_pt])
            plt.show()
        except Exception as e:
            print(e)
