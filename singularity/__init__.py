#file: code/singularity.py
#Copyright (C) 2005 Evil Mr Henry, Phil Bordelon, Brian Reid, MestreLion
#This file is part of Endgame: Singularity.

#Endgame: Singularity is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.

#Endgame: Singularity is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#A full copy of this license is provided in GPL.txt

#This file sets up initial values from command line and preferences file,
# initialize hardware, load data files and show main screen. Do not execute it
# directly. use ../singularity.py instead.

from __future__ import absolute_import


__version__ = "1.0a1"
__release_commit__ = '$Format:%H$'
if __release_commit__[1:-1] == 'Format:%H':
    try:
        import subprocess
        __release_commit__ = subprocess.check_output(['git', 'describe', '--tags']).strip().decode('utf-8')
    except Exception:
        __release_commit__ = 'N/A'

    __full_version__ = "%s (commit: %s)" % (__version__,  __release_commit__)
else:
    __full_version__ = __version__

