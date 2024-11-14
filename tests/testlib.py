import os

_fail=False

def assertTrue(test, text="assertion failed"):
    if not test:
        fail(text)

def shell(arg):
    exitcode = os.waitstatus_to_exitcode(os.system(arg))
    if exitcode > 128:
        return exitcode - 256
    else:
        return exitcode

def fail(arg):
    global _fail
    _fail=True
    print(arg)
    exit(1)

def ok():
    exit(0)
