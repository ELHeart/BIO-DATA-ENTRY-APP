# BIO-CAP is a python based Bio-data collection application currently under development.
# in this repository you will find detailed information about this application in the README file attached.
# Kindly assist with any errors or bugs you may find in the program.

def data_entry():
    # Introduction to the software.
    print("***********************************************************")
    print("Hello and Welcome to BIO-CAP. A Bio-data Entry Application.")
    print("Kindly follow all instructions carefully.")
    print("Contact the System administrator if you encounter any issues.")
    print("***********************************************************")

    # User consent
    print("***********************************************************")
    print("Enter 1 to begin bio-data entry or 0 to cancel.")
    entry = int(input())

    # Consent entry correction and re-entry point
    while entry != 1 and entry != 0:
        print(" Invalid input!!! Enter 1 or 0")
        entry = int(input())
    print("***********************************************************")

    # Data Entry
    if entry == 1:
        print("Bio-data entry begins")
        print("*******************************************")
        print("Enter your First Name: ")
        first_name = str(input())
        print("Enter your Middle Name(Skip if none): ")
        mid_name = str(input())
        print("Enter your Last Name: ")
        last_name = str(input())
        print("Enter your Age: ")
        age = int(input())
        print("End of Bio-data Entry")

        # Data Display
        print("*******************************************")
        print("Entry Details")
        print("*******************************************")
        print("Full Name: ", (first_name + " " + mid_name + " " + last_name))
        print("Age: ", age)
        print("*******************************************")

        # Statement breaks program when user cancels
    elif entry == 0:
        print("Bio-data entry was cancelled by the user!")
        print("Thank You")

    # New Data Input Point
    print("***********************************************************")
    print(" ")
    print("***********************************************************")
    print("Submit new bio-data form? Enter 1 to begin and 0 to exit")
    print("***********************************************************")
    new_data = int(input())

    # New data consent correction and re-entry point
    while new_data != 1 and new_data != 0:
        print(" Invalid input!!! Enter 1 or 0")
        new_data = int(input())
    if new_data == 1:
        data_entry()

    # Application exits here.
    elif new_data == 0:
        print("Application exit successfully!!!")
        print("Thank you for using BIO-CAP!")
        print("***********************************************************")
        print("***APPLICATION DISABLED***")


# MAIN PROGRAM CODES AFTER FUNCTION DECLARATION
# Starter Entry
print(" ")
print("***ENTER 1 TO START APPLICATION OR 0 TO EXIT***")
start = int(input())

# START entry correction and re-entry
while start != 1 and start != 0:
    print(" Invalid input!!! Enter 1 or 0")
    start = int(input())

# Bio-data Input begins if START is 1.
if start == 1:
    data_entry()

# Application close if START is 0
elif start == 0:
    print("***APPLICATION DISABLED***")
