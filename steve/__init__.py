import os
import os.path as op

import appdirs

APPNAME     = 'StEVE'
APPAUTHOR   = 'Page Arkanis'

if 'SDE_DB_DIR' in os.environ and os.environ['SDE_DB_DIR']:
    app_data_dir = os.environ['SDE_DB_DIR']
else:
    app_data_dir = appdirs.user_data_dir(APPNAME, APPAUTHOR)

if not op.exists(app_data_dir):
    os.mkdir(app_data_dir)


# import shortcuts
from steve.backend.sqlitedb import SDB
from steve.assets           import Assets
from steve.universe         import Universe

Assets   = Assets()
Universe = Universe()

