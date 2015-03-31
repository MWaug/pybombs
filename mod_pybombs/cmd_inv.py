#!/usr/bin/env python2
#
# Copyright 2015 Free Software Foundation, Inc.
#
# This file is part of PyBOMBS
#
# PyBOMBS is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# PyBOMBS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyBOMBS; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#
""" PyBOMBS command: Git inv of modules """

from mod_pybombs import *
import pybombs_ops as pybombs_ops

class PyBombsInv(PyBombsCmd):
    """ show or update inventory values """
    name = 'inv'

    def __init__(self):
        PyBombsCmd.__init__(self)
        self._key = None
        self._val = None

    def get_usage_str(self):
        """ Returns a 'usage' string specific for this command. """
        usage_str = """
        inv             - show inventory values
        inv <k>         - clear inventory value for k
        inv <k> <v>     - update local package k inventory value to v
        """
        return usage_str


    def setup(self, options, args):
        if len(args) >= 1:
            self._key = args[0]
        if len(args) >= 2:
            self._val = args[0]
        if len(args) > 2:
            self.parser.error("Command 'inv' accepts at most 2 arguments")

    def run(self):
        " Go, go, go! "
        if self._key is None:
            pybombs_ops.inv.show()
        else:
            pybombs_ops.inventory_set(self._key, self._val)
