from models import Building, Fee, Insurance, Loan, Location, Tax

'''
data = {
    "building": Building object containing a list of units,
    "insurance": Insurance object,
    "fee": Fees object,
    "loan": Loan object,
    "location": Locatoion object,
    "tax": Tax object,
}
'''


class Data:
    def __init__(self):
        self.data = {}
        self.data['building'] = Building()
        self.data['fee'] = Fee()
        self.data['insurance'] = Insurance()
        self.data['loan'] = Loan()
        self.data['location'] = Location()
        self.data['tax'] = Tax()

    def getData(self):
        return self.data