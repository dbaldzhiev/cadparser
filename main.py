import getopt
import sys

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
    cadFileObject = {}
    cadFileText = cadutils.opener(filename)
    cadfileItems = cadutils.ReadCadastralFile(cadFileText)
    # cadFileObject.update({"HEADER":cadutils.Header(cadFileText)})
    # cadFileObject.update({"CADASTER":cadutils.Cadaster(cadFileText)})
    # r=a.CadasterLayer.gepointObj[0]
    print("test")
