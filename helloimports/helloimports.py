#!/usr/bin/env python

__version__ = '0.1.0'
__url__ = 'PROJECT URL'
__email__ = 'PROJECTAUTHOR@EXAMPLE.COM'
__license__ = 'PROJECT LICENSE GOES HERE, BSD, MIT, GPL, ETC.'
__description__ = 'PROJECT DESCRIPTION GOES HERE'
helloimports_info = """
helloimports - {0} - {1} License

{2}

email: {3} url: {4}

Usage:
   helloimports [options]

Options:

   --print-hello-subdir       # prints hello subdir
   
   --print-hello-samedir      # prints hello samedir

   -h, --help                 # Show this help message and quit

   -v, --version              # Show version number and quit

""".format(__version__, __license__, __description__, __email__, __url__)

import sys 
import getopt 

from .subdir.hellosubdir import HelloSubdir
from .hellosamedir import HelloSamedir

def usage():
    print(helloimports_info)

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv", 
                                                 ["print-hello-subdir",
                                                  "print-hello-samedir",
                                                  "help",
                                                  "version",])
    except getopt.GetoptError as err:
        print(str(err)) #prints err msgs like "option -f not recognized"
        # print usage/help info and exit after an error
        usage()
        sys.exit(2)

    for o, a in opts:
        if o == ("--print-hello-subdir"):
            hw = HelloSubdir()
            hw.printsd()
        elif o == ("--print-hello-samedir"):
            hw = HelloSamedir()
            hw.printsd()
        elif o in ("-e", "--example"):
            example_argument = a
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-v", "--version"):
            print("helloimports", __version__)
            sys.exit()
        else:
            assert False, "unhandled option"

if __name__ == "__main__":
    main()
