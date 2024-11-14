import builtins
import traceback

import config
import note

from exceptions import NoRepository

def method(args):
    #print("{0} directory = {1}".format(__name__.rsplit(".")[-1], args.directory))

    try:
        config.load()
        note.new(args.category)

    except NoRepository:
        print("The repository dir must be configured through ZK_REPOSITORY variable or running the command inside the repository dir.")
        exit(-1)
    except Exception as err:
        print(traceback.format_exc())
        exit(-100)

    return 0

parser_get = builtins.subparsers.add_parser(__name__.rsplit(".")[-1], help='creates a new card')
parser_get.add_argument('category', type=str, help='category of the note to be created', default='', nargs='?')
parser_get.set_defaults(func=method)
