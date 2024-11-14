import os, sys

_curdir = os.getcwd()

ZK_CMD="zk.sh"

def begin():
    pathname = os.path.dirname(sys.argv[0])

    os.environ['PATH'] += os.pathsep + os.path.abspath(os.path.join(pathname,".."))
    return

def end():
    global _curdir
    os.chdir(_curdir)
