from steve.backend.sqlitedb import SDB
from steve.activity         import Activity


class Industry(object):
    
    
    def __init__(self):
        self._activities = {}
        
        
    @property
    def activity(self):
        if len(self._activities) == 0:
            for entry in SDB.queryAll('SELECT * from ramActivities'):
                _object = Activity(self, entry)
                self._activities[_object.uid]  = _object
                self._activities[_object.name] = _object
        
        return self._activities
