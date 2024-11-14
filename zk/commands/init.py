import argparse
import builtins
import traceback
from pathlib import Path

import config
from exceptions import DirectoryNotEmpty, CannotInitializeInsideRepositoryException, DirectoryAlreadyInitializedException

def method(args):
    #print("{0} directory = {1}".format(__name__.rsplit(".")[-1], args.directory))

    try:
        dir = Path(args.directory).resolve()
        config.init(dir)
    except DirectoryNotEmpty:
        print("The directory to initialize is not empty.")
        exit(-10)
    except CannotInitializeInsideRepositoryException:
        print("You are trying to initialize inside a already initialized repository.")
        exit(-11)
    except DirectoryAlreadyInitializedException:
        print("Directory already initialized.")
        exit(-12)
    except Exception as err:
        print(traceback.format_exc())
        print("Cannot initialize directory. Do you have permission to create directory?")
        exit(-100)

    return 0

parser_get = builtins.subparsers.add_parser(__name__.rsplit(".")[-1], help='initilizes the repository')
parser_get.add_argument('directory', type=str, help='directory name to initialize (defaults to current directory)', default='', nargs='?')
parser_get.set_defaults(func=method)
