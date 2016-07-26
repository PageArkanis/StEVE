from hashlib import md5

import bz2
import os.path as op
import urllib

import sqlite3 as lite

from steve import app_data_dir


class SqliteDB(object):
    
    DB_FILE   = 'sqlite-latest.sqlite'
    R_ARCHIVE = "https://www.fuzzwork.co.uk/dump/%s.bz2" % DB_FILE
    L_ARCHIVE = op.join(app_data_dir, "%s.bz2" % DB_FILE)

    
    def __init__(self):

        # check for update
        try:
            if SqliteDB.update(SqliteDB.R_ARCHIVE, SqliteDB.L_ARCHIVE):
                SqliteDB.unpack()
        except IOError:
            print 'Could not perform update check: IOError'

        self.db_file          = op.join(app_data_dir, SqliteDB.DB_FILE)
        self.con              = lite.connect(self.db_file)
        self.con.text_factory = str
        self.con.row_factory  = lite.Row


    def __del__(self):
        self.con.close()


    def queryOne(self, query):
        assert isinstance(query, str)
        cur = self.con.cursor()    
        cur.execute(query)
        return cur.fetchone()


    def queryAll(self, query):
        assert isinstance(query, str)
        cur = self.con.cursor()    
        cur.execute(query)
        return cur.fetchall()


    @staticmethod
    def unpack():
        filepath    = SqliteDB.L_ARCHIVE
        newfilepath = op.splitext(SqliteDB.L_ARCHIVE)[0]
        with open(newfilepath, 'wb') as new_file, bz2.BZ2File(filepath, 'rb') as f:
            for data in iter(lambda : f.read(100 * 1024), b''):
                new_file.write(data)


    @staticmethod
    def update(remote_file, local_file):

        # get local md5 checksum
        local_md5 = None
        if op.isfile(local_file):
            with open(local_file, 'rb') as f:
                local_md5 = md5(f.read()).hexdigest()
    
    
        # get remote file if it does not exist locally
        if local_md5 is None:
            print 'Download: %s -> %s' % (remote_file, local_file),
            urllib.URLopener().retrieve(remote_file, local_file)
            print 'finished.'
            return True
    
        # continue to check
        else:
            
            # download remote md5 checksum
            remote_md5 = urllib.urlopen(remote_file + '.md5').read()
            remote_md5 = remote_md5.split()[0]
            
            if local_md5 != remote_md5:
                print 'Download: %s -> %s' % (remote_file, local_file),
                urllib.URLopener().retrieve(remote_file, local_file)
                print 'finished.'
                return True
            
        return False


SDB = SqliteDB()