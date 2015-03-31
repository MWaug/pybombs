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
""" PyBOMBS command: Git config of modules """

from mod_pybombs import *
import pybombs_ops as pybombs_ops

class PyBombsConfig(PyBombsCmd):
    """ Show or set configuration settings """
    name = 'config'

    def __init__(self):
        PyBombsCmd.__init__(self)

    def setup(self, options, args):
        pass

    def run(self):
        pybombs_ops.config();
        if(len(args) == 0):
            pybombs_ops.config_print()
        elif(len(args) == 1):
            pybombs_ops.config_get(args[0])
        elif(len(args) == 2):
            pybombs_ops.config_set(args[0], args[1])
        else:
            parser.error("Command 'config' accepts at most 2 arguments")
