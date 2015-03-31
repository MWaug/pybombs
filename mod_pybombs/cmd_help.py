#
# Copyright 2013 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#
""" The help module """

import sys
from mod_pybombs import *

def get_command_from_argv(possible_cmds):
    """ Read the requested command from argv. This can't be done with optparse,
    since the option parser isn't defined before the command is known, and
    optparse throws an error."""
    for arg in sys.argv:
        if arg[0] != "-" and arg in possible_cmds:
            return arg
    return None

def print_class_descriptions():
    """ Go through all PyBombs* classes and print their name,
        alias and description. """
    desclist = []
    for gvar in globals().values():
        try:
            if issubclass(gvar, PyBombsCmd) and not gvar.name in (PyBombsHelp.name, PyBombsCmd.name) and not gvar.hidden:
                desclist.append((gvar.name, gvar.__doc__))
        except (TypeError, AttributeError):
            pass
    print '  Name       Description'
    print '======================================================'
    for description in desclist:
        print '  %-8s  %s' % description


class PyBombsHelp(PyBombsCmd):
    """ Show some help. """
    name = 'help'
    usage = """
    PyBOMBS yo
    """

    def __init__(self):
        PyBombsCmd.__init__(self)

    def setup(self, options, args):
        pass

    def run(self):
        cmd_dict = get_class_dict(globals().values())
        cmds = cmd_dict.keys()
        cmds.remove(self.name)
        help_requested_for = get_command_from_argv(cmds)
        if help_requested_for is None:
            print 'Usage:' + self.usage
            print '\nList of possible commands:\n'
            print_class_descriptions()
            return
        cmd_dict[help_requested_for]().setup_parser().print_help()

