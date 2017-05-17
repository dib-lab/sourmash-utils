# -*- coding: utf-8 -*-

import sys

from . import subtract


def main(args=None):
    if args is None:
        # TODO: parse from sys.argv
        args = sys.argv[1:]
    commands = {
      'subtract': subtract.main,
    }
    cmd = args[0]
    cmd_args = args[1:]
    return commands[cmd](cmd_args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[2:]))
