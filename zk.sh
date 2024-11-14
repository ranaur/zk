#!/bin/sh
ROOT_DIR="$(dirname "$(realpath "$BASH_SOURCE[0]")")"

python3 "$ROOT_DIR/zk" "$@"

exit $?
