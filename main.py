import sys

from matplotlib import pyplot as plt

import cadutils
import config
import dxfmaker

if __name__ == '__main__':
    filename = sys.argv[1]

    cadobject = cadutils.ParseFile(filename)
    dxfmaker.makedxf(cadobject)
    # kmlmaker.makekml(filename, cadFileItems)

    if config.debug:
        plt.figure()
        for c in cadobject.CadasterLayer.contourObj:
            plt.suptitle(c.cid, fontsize=16)
            if c.pgon_pt:
                plt.plot([x[0] for x in c.pgon_pt], [y[1] for y in c.pgon_pt])
        plt.show()
