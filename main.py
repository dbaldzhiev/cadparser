import getopt
import sys

try:
    import matplotlib.pyplot as plt
except Exception:
    pass
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


def pl(data):
    for con in data.CadasterLayer.contourObj:
        try:
            plt.figure()
            plt.suptitle(con.cid, fontsize=16)
            plt.plot([x[0] for x in con.pgon_ext], [y[1] for y in con.pgon_ext])
            if len(con.pgon_holes) > 0:
                plt.figure()
                plt.plot([x[0] for x in con.pgon_ext], [y[1] for y in con.pgon_ext])
                for hole in con.pgon_holes:
                    plt.plot([x[0] for x in hole], [y[1] for y in hole])
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
if __name__ == '__main__':
    cadFileText = cadutils.opener(filename)
    cadfileItems = cadutils.ReadCadastralFile(cadFileText)
    plsec(cadfileItems)

    # a = test.tests()
    print("ab")
