import tempfile
import os
from pathlib import Path
import zktest
from zktest import ZK_CMD
import testlib

zktest.begin()

try:
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname)

        testlib.shell(f"{ZK_CMD} init")

        ret = testlib.shell(f"{ZK_CMD} new entry")
        testlib.assertTrue(ret == 0, f"exception: unexpected exit code {ret}");


except Exception as exp:
    testlib.fail(exp)

zktest.end()
testlib.fail("Still developing ...")
testlib.ok()
