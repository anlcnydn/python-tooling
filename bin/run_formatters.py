#!/usr/bin/env python
"""
Runs black and isort with predefined configurations.

If a certain path passed as an argument, it will run on that path,
otherwise, run on `python_tooling` and `tests` by default.

If '-c' passed as second argument, it will only check the code not format it.

For local usage `path` must always be the last argument.

./run_formatters.py <path>

or

./run_formatters.py -c <path>

"""

import os
import sys


def run_black(path=None, check=False):
    black_arguments = ["black"]
    if check:
        black_arguments.append("--check")

    if path:
        black_arguments.append(path)
    else:
        black_arguments.append(".")

    os.system(" ".join(black_arguments))


def run_isort(path=None, check=False):
    isort_arguments = ["isort"]
    if check:
        isort_arguments.append("--check")

    if path:
        isort_arguments.append(path)
    else:
        isort_arguments.append(".")

    os.system(" ".join(isort_arguments))


def format_all():
    run_black()
    run_isort()


def check_all():
    run_black(check=True)
    run_isort(check=True)


def format_path(path):
    run_black(path=path)
    run_isort(path=path)


def check_path(path):
    run_black(path, check=True)
    run_isort(path, check=True)


def run():
    # check all
    if len(sys.argv) > 1 and "-c" in sys.argv:
        check_all()
    # format path
    elif len(sys.argv) > 1 and "-c" not in sys.argv:
        path = sys.argv[1]
        format_path(path)
    # check path
    elif len(sys.argv) > 2 and "-c" in sys.argv:
        path = sys.argv[2]
        check_path(path)
    # format all
    else:
        format_all()


if __name__ == "__main__":
    run()
