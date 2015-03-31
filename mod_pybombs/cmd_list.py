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
""" PyBOMBS command: List modules """

from mod_pybombs import *
import pybombs_ops as pybombs_ops

class PyBombsList(PyBombsCmd):
    """ show installed & available packages """
    name = 'list'

    def __init__(self):
        PyBombsCmd.__init__(self)

    def setup(self, options, args):
        pass

    def run(self):
        " Go, go, go! "
        pybombs_ops.pkglist()

