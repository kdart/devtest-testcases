# python3

"""Demo module for showing some framework features.

Provides a special test case that enters an interactive prompt within the test
procedure. The user can then invoke any method and inspect to config and
testbed interactively. Useful for demos and learning the API.
"""

from devtest.qa import bases
from devtest.qa import repl


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
        cons = repl.InteractiveConsole(namespace=locals(), io=self.UI._io,
                                       ps1="TestCase> ")
        cons.interact(banner="Now try out the methods and other functions.")

# vim:ts=4:sw=4:softtabstop=0:smarttab
