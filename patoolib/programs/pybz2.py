# -*- coding: utf-8 -*-
# Copyright (C) 2012 Bastian Kleineidam
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Archive commands for the bz2 Python module."""
from patoolib import util
try:
    # try external bz2file module with multi-stream support
    import bz2file as bz2
except ImportError:
    import bz2

READ_SIZE_BYTES = 1024*1024

def extract_bzip2 (archive, encoding, cmd, **kwargs):
    """Extract a BZIP2 archive with the bz2 Python module functionality."""
    verbose = kwargs['verbose']
    if verbose:
        util.log_info('extracting %s...' % archive)
    targetname = util.get_single_outfile(kwargs['outdir'], archive)
    bz2file = bz2.BZ2File(archive)
    try:
        targetfile = open(targetname, 'wb')
        try:
            data = bz2file.read(READ_SIZE_BYTES)
            while data:
                targetfile.write(data)
                data = bz2file.read(READ_SIZE_BYTES)
        finally:
            targetfile.close()
    finally:
        bz2file.close()
    if verbose:
        util.log_info('... extracted to %s' % targetname)
    return None