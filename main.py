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
    cadFileText = cadutils.opener(filename)
    cadfileItems = cadutils.ReadCadastralFile(cadFileText)
    # test.tests()
    # pl(cadfileItems)

    # a = test.tests()
    print("ab")
