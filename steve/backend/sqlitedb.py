import bz2
from hashlib import md5
import logging
import os.path as op
import sqlite3 as lite
import sys
import urllib


from steve import app_data_dir
from __builtin__ import str

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
            logging.warning('Could not perform update check. Check your connection.') 

        self.db_file = op.join(app_data_dir, SqliteDB.DB_FILE)


    def __del__(self):
        self.con.close()

    @property
    def con(self):
        connection = lite.connect(self.db_file)
        connection.text_factory = str
        connection.row_factory  = lite.Row
        return connection
        

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
            logging.info('Download: %s -> %s' % (remote_file, local_file))
            sys.stdout.flush()
            urllib.URLopener().retrieve(remote_file, local_file)
            logging.info('finished.')
            return True
    
        # continue to check
        else:
            
            # download remote md5 checksum
            remote_md5 = urllib.urlopen(remote_file + '.md5').read()
            remote_md5 = remote_md5.split()[0]
            
            if local_md5 != remote_md5:
                logging.info('Download: %s -> %s' % (remote_file, local_file))
                sys.stdout.flush()
                urllib.URLopener().retrieve(remote_file, local_file)
                logging.info('finished.')
                return True
            
        return False


SDB = SqliteDB()