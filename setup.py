####################################################################################################
#    Copyright (C) 2016 by Page Arkanis                                                            #
#    <pagearkanis@gmail.com>                                                                       #
#                                                                                                  #
#    This file is part of StEVE (A Static Data Access API for EVE Online).                         #
#                                                                                                  #
#    StEVE is free software: you can redistribute it and/or modify it under the terms of the       #
#    GNU Affero General Public License as published by the Free Software Foundation, either        #
#    version 3 of the License, or (at your option) any later version.                              #
#                                                                                                  #
#    StEVE is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;            #
#    without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.     #
#    See the GNU Affero General Public License for more details.                                   #
#                                                                                                  #
#    You should have received a copy of the GNU Affero General Public License                      #
#    along with StEVE.  If not, see <http://www.gnu.org/licenses/>.                                #
####################################################################################################
import os

from setuptools import setup, find_packages

version = open(os.path.join("steve", "version.txt")).read().strip()

setup( name                 = 'StEVE',
       version              = version,
       description          = "A Static Data Access API for EVE Online",
       long_description     = open("README.md").read(),
       # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
       classifiers          = [
         "Programming Language :: Python",
         "Topic :: Software Development :: Libraries :: Python Modules",
         ],
       keywords             = '',
       author               = 'Page Arkanis',
       author_email         = 'pagearkanis@gmail.com',
       url                  = '',
       license              = 'AGPL v3',
       packages             = find_packages(exclude=['ez_setup']),
       namespace_packages   = [],
       include_package_data = True,
       zip_safe             = False,
       install_requires     = [
           'setuptools',
           # -*- Extra requirements: -*-
           'appdirs',
       ],
       entry_points         = """
       # -*- Entry points: -*-
       """,

       scripts = [
       ]
     )
