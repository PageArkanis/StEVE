
class StationType(object):
    
    
    def __init__(self, universe, data):
        
        self.universe                   = universe
        self.uid                        = data[0]
        self.dockEntryX                 = data[1]
        self.dockEntryY                 = data[2]
        self.dockEntryZ                 = data[3]
        self.dockOrientationX           = data[4]
        self.dockOrientationY           = data[5]
        self.dockOrientationZ           = data[6]
        self.operationID                = data[7]
        self.officeSlots                = data[8]
        self.reprocessingEfficiency     = data[9]
        self.conquerable                = data[10]
