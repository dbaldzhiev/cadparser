# VERSION 4.0
import sys
import matplotlib.pyplot as plt
from utils import ReadCadastralFile
import config
import dxfmaker
import kmlmaker

def main():
    filename = sys.argv[1]
    cadobject = ReadCadastralFile(filename)
    dxfmaker.makedxf(cadobject)
    kmlmaker.makekml(cadobject)
    plot_cadastral_data(cadobject)

def plot_cadastral_data(cadobject):
    if config.debug:
        try:
            plt.figure()
            for contour in cadobject.CadasterLayer.contourObj:
                plt.suptitle(contour.cid, fontsize=16)
                if contour.pgon_pt:
                    plt.plot([x[0] for x in contour.pgon_pt], [y[1] for y in contour.pgon_pt])
            plt.show()
        except Exception as e:
            print(f"Error plotting cadastral data: {e}")

if __name__ == '__main__':
    main()
