import yaml
import os
from pathlib import Path
from exceptions import DirectoryNotEmpty, CannotInitializeInsideRepositoryException, DirectoryAlreadyInitializedException, NoRepository

from defaultconfig import CONFIG_DIR, CONFIG_FILE, default_config

def init(dir):
    p = Path(dir).resolve().parent
    while p.parent != p:
        if os.path.isdir(Path(p, CONFIG_DIR)):
            raise CannotInitializeInsideRepositoryException()
        p = p.parent

    if os.path.isdir(dir):
        if os.path.isdir(Path(dir, CONFIG_DIR)):
            raise DirectoryAlreadyInitializedException()
        if os.listdir(dir):
            raise DirectoryNotEmpty()
    else:
        os.mkdir(dir)

    os.mkdir(Path(dir, CONFIG_DIR))

    config_file = Path(dir, CONFIG_DIR, CONFIG_FILE)

    with config_file.open("w") as stream:
        global _config
        yaml.dump(default_config, stream, encoding='utf-8')

    _load(dir)

def _load(dir):
    config_dir = Path(dir, CONFIG_DIR)
    if config_dir.is_dir():
        try:
            config_file = Path(dir, CONFIG_DIR, CONFIG_FILE)

            with config_file.open() as stream:
                global _config
                _config=yaml.safe_load(stream)
        except Exception as exc:
            return False

        return True
    else:
        return False

def _validate_config():
    assert(isloaded())
    global _repository_config_dir
    global _config
    _repository_config_dir = Path(_repository_path, CONFIG_DIR)

    for key in _config["categories"].keys():
        categorydir = Path(_repository_path, key)
        if not os.path.isdir(categorydir):
            os.mkdir(categorydir)

        if not os.path.isdir(categorydir):
            os.mkdir(categorydir)

def isloaded():
    global _repository_path
    return _repository_path != None

def load():
    global _repository_path
    global _repository_config_dir
    global _repository_config_dir

    if isloaded():
        return

    env_path = os.getenv("ZK_REPOSITORY")
    if env_path:
        _load(env_path)
    else: # if there is no env path, try current directory or it's parents
        p = Path(".").resolve()

        while p.parent != p:
            if _load(p) == True:
                _repository_path = p
                break
            p = p.parent

    if isloaded():
        _validate_config()
    else:
        raise NoRepositoty

def get(name):
    # TODO decode (split) dot notation?
    return _config[name]

_repository_path = None
_repository_config_dir = None
_config = None
