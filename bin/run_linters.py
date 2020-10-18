#!/usr/bin/env python
"""
Runs pylint and bandit with predefined configurations.

If a certain path passed as an argument, it will run on that path,
otherwise, run on `python_tooling` and `tests` by default.

"""

import os
import sys

from pylint.lint import Run

PYLINT_CONFIG_FILE = ".config/pylintrc"
BANDIT_CONFIG_FILE = ".config/bandit.yml"
SOURCE_MODULE = "python_tooling"
TESTS_MODULE = "tests"


def run_pylint(path=None):
    pylint_arguments = ["--rcfile", PYLINT_CONFIG_FILE]
    if path:
        pylint_arguments.append(path)
    else:
        pylint_arguments.append(SOURCE_MODULE)
        pylint_arguments.append(TESTS_MODULE)

    Run(pylint_arguments, do_exit=False)


def run_bandit(path=None):
    print("Running bandit")
    bandit_arguments = ["bandit", "-r", "-c", BANDIT_CONFIG_FILE]
    if path:
        bandit_arguments.append(path)
    else:
        bandit_arguments.append(SOURCE_MODULE)

    os.system(" ".join(bandit_arguments))


def run():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        run_pylint(path=path)
        run_bandit(path=path)
    else:
        run_pylint()
        run_bandit()


if __name__ == "__main__":
    run()
