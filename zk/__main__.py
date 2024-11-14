#!/usr/bin/env python
import argparse
import builtins
import inspect

import config

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Zettelkasten in plain files')
    builtins.subparsers = parser.add_subparsers()
    import commands

    args = parser.parse_args()

    if (hasattr(args, 'func') and inspect.isfunction(args.func)):
        try:
            exit(args.func(args))
        except Exception as e:
            print(("error: " + e.__class__.__name__ + " " + str(e)).rstrip())
            exit(1)
    else:
        print(f"Invalid command. Type zk -h to get the full command list.")

        #parser.print_help()

