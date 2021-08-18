import Unit
'''
    buildings
        year built
        lot size square feet
        units - 1 for single family or multiple for multi-family
'''

class Building:
    def __init__(self):
        self.yearBuilt = None # Int
        self.lotSizeSquareFeet = None # Int
        self.units = [] # Int