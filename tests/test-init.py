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

        testlib.shell(f"{ZK_CMD} init test")

        # good case
        if not os.path.isdir(Path("test",".zk")):
            testlib.fail("Directory .zk not created!")

        if not os.path.isfile(Path("test",".zk","config")):
            testlib.fail("Config file not created!")

        # empty directory
        testlib.shell("rm -R test/.zk > /dev/null")
        ret = testlib.shell(f"{ZK_CMD} init test > /dev/null")
        if not os.path.isdir(Path("test",".zk")):
            testlib.fail("Directory .zk not created!")

        if not os.path.isfile(Path("test",".zk","config")):
            testlib.fail("Config file not created!")

        # exception: initialize in an already initialized directory
        ret = testlib.shell(f"{ZK_CMD} init test > /dev/null")
        testlib.assertTrue(ret == -12, "exception: initialize in an already initialized directory {0}".format(ret));

        # exception: initilizing in a non-empty directory
        os.mkdir("test2")
        os.mkdir(Path("test2","nonempty"))
        ret = testlib.shell(f"{ZK_CMD} init test2> /dev/null")
        testlib.assertTrue(ret == -10, "exception: initilizing in a non-empty directory");

        # exception: initilize inside another repository
        ret = testlib.shell(f"{ZK_CMD} init test/inside > /dev/null")
        testlib.assertTrue(ret == -11, "exception: initilize inside another repository");
except Exception as exp:
    testlib.fail(exp)

zktest.end()
testlib.ok()
