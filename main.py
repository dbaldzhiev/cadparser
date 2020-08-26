import getopt
import sys
from matplotlib import pyplot as plt

import cadutils

# Get the arguments from the command-line except the filename
argv = sys.argv[1:]
filename = ""

try:
    opts, args = getopt.getopt(argv, 'f:o:', ['filename', 'options'])
    if len(opts) == 0 and len(opts) > 2:
        print('usage: add.py -f <first_operand> -o <second_operand>')
    else:
        # Iterate the options and get the corresponding values
        for opt, arg in opts:
            if opt == "-f":
                filename = arg
except getopt.GetoptError:
    # Print something useful
    print('usage: add.py -a <first_operand> -b <second_operand>')
    sys.exit(2)

if __name__ == '__main__':
    cadFileText = cadutils.opener(filename)
    cadFileItems = cadutils.ReadCadastralFile(cadFileText)
    for c in cadFileItems.CadasterLayer.contourObj:
        if c.pgon_bad_flag:
            plt.figure()
            plt.suptitle(c.cid, fontsize=16)

            if c.pgon_pt:
                plt.plot([x[0] for x in c.pgon_pt], [y[1] for y in c.pgon_pt])

            plt.show()
    #test.tests()
    # pl(cadFileItems)
    # a = test.tests()
    print("ab")
