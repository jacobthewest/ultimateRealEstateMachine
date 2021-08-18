import os

USER_EMAIL = None
DOWN_PAYMENT = None
MONTHLY_DEBT_PAYMENTS = None
FHA_LOAN = None
OPEN_TO_LANDLORD = None
CLEAR = "\n" * 10
ANALYZE_A_DEAL = None
SEARCH_AREA = None
STATE = None


def greet():
    print("\nHello! This is a tool to analyze and find real estate deals.")
    print("We will start by gathering some basic information about you.\n")


def getEmail():
    USER_EMAIL = input("Please input your email: ")
    response = None
    isValidEmail = False
    doubleCheck = True

    while not isValidEmail:
        if doubleCheck:
            response = input("\tDouble checking, is '" + USER_EMAIL + "' your email? Type 'y' or 'n': ")
            if response == 'n':
                USER_EMAIL = input("Please input your email again: ")
            elif response == 'y':
                printTransition("Thank you for your email!")
                isValidEmail = True

def getBasicFinancialInformation():
    print(CLEAR)
    printHeader("Now we'll get some basic information from you")
    DOWN_PAYMENT = float(input("How much money do you have for a down payment? -> $").replace(',', ''))
    MONTHLY_DEBT_PAYMENTS = float(input("How much are your TOTAL monthly debt payments? " +
                                        "i.e. 200.32 or 50 -> $").replace(',', ''))

    FHA_LOAN = input("Are you a first-time home buyer? Or will you live here for 1+ years? Type 'y' or 'n' -> ")
    if FHA_LOAN == 'y':
        FHA_LOAN = True
    else:
        FHA_LOAN = False

    OPEN_TO_LANDLORD = input("Are you open to landlord? Or host on AirBnb? Type 'y' or 'n' -> ")
    if OPEN_TO_LANDLORD == 'y':
        OPEN_TO_LANDLORD = True
    else:
        OPEN_TO_LANDLORD = False

    printTransition("Thanks for the basic information!")

def printTransition(message):
    print(CLEAR)
    print(message)
    print(CLEAR)

def printHeader(header):
    print("--------------------" + header + "--------------------")

def getAnalyzeorFindMessage():
    if ANALYZE_A_DEAL:
        return 'analyze a deal.'
    else:
        return 'find a deal.'



def getUserUseCase():
    printHeader("Let's See How We Can Help You?")
    response = input("Do you want to find a deal (type '1') or analyze a deal (type '2')? -> ")
    if response == '1':
        ANALYZE_A_DEAL = False
    elif response == '2':
        ANALYZE_A_DEAL = True

    printTransition('Ok! We can definitely help you ' + getAnalyzeorFindMessage())

def getAreaOfFocus():
    printHeader("Now we'll get some info about your location of interest")
    STATE = input("What state should we search in? i.e. UT or AZ -> ")
    print("How should we search?")
    print("\tBy area code? (type '1')")
    print("\tBy city? (type '2')")
    print("\tBy county? (type '3')")
    response = input("\tWhat is your choice? -> ")

    if response == '1':
        SEARCH_AREA = int(input("Enter the area code you're interested in -> "))
    elif response == '2':
        SEARCH_AREA = input("Enter the city you're interested in i.e. Tempe or Orem -> ")
    elif response == '3':
        SEARCH_AREA = input("Enter the county you're interested in. i.e. Salt Lake or Maricopa -> ")

    printTransition(str(SEARCH_AREA) + ' is a great place!')

def printPropertySpecificsMessages():
    if ANALYZE_A_DEAL:
        printHeader('Tell Us About The Deal You Want to Analyze')
    elif not ANALYZE_A_DEAL and OPEN_TO_LANDLORD:
        printHeader("Tell Us About What You're Thinking")
        print("You've chosen to " + getAnalyzeorFindMessage() + ". You've also indicated +"
              "that you are open to landlord or be an AirBnb host. That's great! Way to be " +
              "entrepreneurially minded. Good for you. You deserve more in your life and " +
              "this is a great first step.\n")
        print('We are going to ask you some basic information about what you want in a property')
        print("Please answer the following questions as vaguely as possible. Why? " +
              " Because the Ultimate Real Estate Machine will find the best deals " +
              "for you and will provide you a list of deals that only make financial sense to you.")
    else:
        printHeader('Tell Us About Your Dream Property')
        print("Remember, the more vague you are the more properties we'll find for you.")

def getPropertySpecifics():
    printPropertySpecificsMessages()
    print("You can leave an input blank by just hitting enter.")

    BED_MIN = int(input("Min Beds: "))
    BED_MAX = int(input("Max Beds: "))
    BATH_MIN = int(input("Min Baths: "))
    BATH_MAX = float(input("Min Baths: "))
    SQUARE_FEET_MIN = int(input("Minimum Square Feet: "))
    SQUARE_FEET_MAX = int(input("Maximum Square Feet: "))
    LOT_SIZE_MIN = int(input("Min Lot Size: "))
    LOT_SIZE_MAX = int(input("Max Lot Size: "))
    YEAR_BUILT_MIN = int(input("Oldest Year Built: "))
    YEAR_BUILT_MAX = int(input("Newest Year Built: "))
    HOA_MIN = int(input("Min Monthly HOA Payment"))
    HOA_MAX = int(input("Max Monthly HOA Payment"))



def startProgram():
    while(True):
        pass


greet()
getEmail()
getBasicFinancialInformation()
getAreaOfFocus()
getUserUseCase()
getPropertySpecifics()
#startProgram()