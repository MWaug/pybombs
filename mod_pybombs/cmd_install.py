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
""" PyBOMBS command: Install """

from mod_pybombs import *
import pybombs_ops as pybombs_ops

class PyBombsInstall(PyBombsCmd):
    """ Install a package """
    name = 'install'

    def __init__(self):
        PyBombsCmd.__init__(self, load_recipes=True)

    def setup_parser(self):
        " Add 'install' specific flags "
        parser = PyBombsCmd.setup_parser(self)
        ogroup = OptionGroup(parser, "Install options")
        ogroup.add_option("--static", action="store_true", default=False,
                help="Install using static options.")
        parser.add_option_group(ogroup)
        return parser

    def setup(self, options, args):
        if len(args) == 0:
            parser.error("Command 'info' requires at least one package")
        self._pkgs = args
        self.opts = options
        self._static = options.static
        pybombs_ops.config_set("static", str(self._static))
        # FIXME This skips the case where --static is not supplied
        # on the cmd line, but is in the config settings


    def run(self):
        " Go, go, go! "
        for p in self._pkgs:
            pybombs_ops.install(p, not self.opts.force);
