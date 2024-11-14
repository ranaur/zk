CONFIG_DIR=".zk"
CONFIG_FILE="config"

default_config = {
    "zk_version": "0.1.0",
    "categories": {
        "entry": {
            "name": "Zettelkasten default entry",
            "metadata": [
                { "name": "Title", "type": "text", "mandatory": True, "default": "" },
                { "name": "Creation Date", "type": "date", "mandatory": True, "default": "@D" },
                { "name": "id", "type": "id", "mandatory": True, "default": "" },
            ],
            "prefix": "ZK"
        },
    },
    "defaultcategory": "entry"
}
