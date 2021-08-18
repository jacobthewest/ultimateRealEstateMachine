'''
    unit
        bed
        bath
        square feet
        owner occupied
        expected rent
        vacancyPercentage
'''

class Unit:
    def __init__(self):
        self.bed = None # Int
        self.bath = None # Float
        self.squareFeet = None # Int
        self.ownerOccupied = None # Boolean
        self.expectedRent = None # Float
        self.vacancyPercentage = None # Float