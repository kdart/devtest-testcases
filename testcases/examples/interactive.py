# python3

"""Demo module for showing some framework features.

Provides a special test case that enters an interactive prompt within the test
procedure. The user can then invoke any method and inspect to config and testbed
interactively. Useful for demos and learning the API.
"""

import sys
import os
import readline
import code

from devtest.qa import bases


class TestCaseConsole(code.InteractiveConsole):
    def __init__(self, locals_):
        super().__init__(locals=locals_, filename=__name__)
        sys.ps1 = "Testcase> "
        sys.ps2 = "....more> "
        readline.set_history_length(1000)
        if sys.platform == "darwin":
            readline.parse_and_bind("^I rl_complete")
        else:
            readline.parse_and_bind("tab: complete")
        readline.parse_and_bind("set horizontal-scroll-mode on")
        readline.parse_and_bind("set page-completions on")
        readline.set_completer_delims(" ")
        self._historyfile = os.path.expandvars("$HOME/.hist_testcase")
        try:
            readline.read_history_file(self._historyfile)
        except FileNotFoundError:
            pass

    def __del__(self):
        readline.write_history_file(self._historyfile)


class InteractiveTest(bases.TestCase):
    """
    Purpose
    -------

    Enable direct interaction of the framework API.

    Pass Criteria
    -------------

    None

    Start Condition
    ---------------

    NA

    End Condition
    -------------

    No change.

    Reference
    ---------

    None

    Procedure
    ---------

    #. Start an interactive interpreter in the context of the execute method.
    """
    PREREQUISITES = []

    def procedure(self, argument=None):
        cons = TestCaseConsole(locals())
        cons.interact(banner="Now try out the methods and other functions.",
                      exitmsg="")

# vim:ts=4:sw=4:softtabstop=0:smarttab
