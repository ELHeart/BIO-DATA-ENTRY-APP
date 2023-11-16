# BIO-CAP is a python based Bio-data collection application currently under development.
# in this repository you will find detailed information about this application in the README file attached.
# Kindly assist with any errors or bugs you may find in the program.

# This Function defines the data input and display.
def data_entry():
    # User consent
    print("***********************************************************")
    print("***  ENTER 1 TO BEGIN ENTRY OR 0 TO CANCEL   ***")
    entry = int(input())

    # Consent entry correction and re-entry point
    while entry != 1 and entry != 0:
        print("***  INVALID INPUT   ***")
        print("***  ENTER 1 OR 0    ***")
        entry = int(input())
    print("***********************************************************")
    print(" ")

    # Data Entry
    if entry == 1:
        print("***  BEGIN BIO-DATA ENTRY    ***")
        print("*******************************************")
        print(" ")
        print("Enter your First Name: ")
        first_name = str(input())
        print("Enter your Middle Name(Skip if none): ")
        mid_name = str(input())
        print("Enter your Last Name: ")
        last_name = str(input())
        print("Enter your Age: ")
        age = int(input())
        print(" ")
        print("***  END OF BIO-DATA ENTRY   ***")

        # Data Display
        print("*******************************************")
        print(" ")
        print("***  ENTRY DETAILS   ***")
        print("*******************************************")
        print(" ")
        print("FULL NAME: ", (first_name + " " + mid_name + " " + last_name))
        print("AGE: ", age)
        print(" ")
        print("***  END ***")
        # New data entry point
        new_data_entry()

        # Statement breaks program when user cancels
    elif entry == 0:
        print("***  ENTRY CANCELLED BY USER ***")
        print("***  APPLICATION DISABLED ***")


# This Function defines the code for new data entry.
def new_data_entry():
    # New Data Input Point
    print(" ")
    print("***********************************************************")
    print("***  NEW ENTRY ***")
    print("***  ENTER 1 TO BEGIN OR 0 TO CANCEL")
    new_data = int(input())

    # New data consent correction and re-entry point
    while new_data != 1 and new_data != 0:
        print("***  INVALID INPUT   ***")
        print("***  ENTER 1 OR 0    ***")
        new_data = int(input())
    if new_data == 1:
        data_entry2()

    # Application exits here.
    elif new_data == 0:
        print("***  ENTRY CANCELLED BY USER ***")
        print("***  APPLICATION DISABLED ***")


def data_entry2():
    print("***  BEGIN BIO-DATA ENTRY    ***")
    print("*******************************************")
    print(" ")
    print("Enter your First Name: ")
    first_name = str(input())
    print("Enter your Middle Name(Skip if none): ")
    mid_name = str(input())
    print("Enter your Last Name: ")
    last_name = str(input())
    print("Enter your Age: ")
    age = int(input())
    print(" ")
    print("***  END OF BIO-DATA ENTRY   ***")
    # Data Display
    print("*******************************************")
    print(" ")
    print("***  ENTRY DETAILS   ***")
    print("*******************************************")
    print(" ")
    print("FULL NAME: ", (first_name + " " + mid_name + " " + last_name))
    print("AGE: ", age)
    print(" ")
    print("***  END ***")
    # New data entry point
    new_data_entry()


# MAIN PROGRAM CODES AFTER FUNCTION DECLARATION
# Program Activation code validation point
print(" ")
print("***  ENTER 1 TO START APPLICATION OR 0 TO EXIT   ***")
start = int(input())

# START entry correction and re-entry
while start != 1 and start != 0:
    print("***  INVALID INPUT   ***")
    print("***  ENTER 1 OR 0    ***")
    start = int(input())

# Application begins if START is 1.
if start == 1:
    print("***********************************************************")
    print("***  WELCOME TO BIO-CAP  ***")
    print("***  KINDLY FOLLOW ALL INSTRUCTIONS CAREFULLY    ***")
    print("***  CONTACT SYSTEM ADMIN IF ANY ISSUES ARISE    ***")
    print("***********************************************************")
    print(" ")
# Data entry point
    data_entry()

# Application is disabled if START is 0
elif start == 0:
    print("***  APPLICATION DISABLED    ***")
