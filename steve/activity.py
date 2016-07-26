

class Activity(object):
    
    
    def __init__(self, industry, data):
        
        self.industry = industry
        
        self.uid            = data[0] 
        self.name           = data[1]
        self.iconNo         = data[2]
        self.description    = data[3]
        self.published      = data[4]
