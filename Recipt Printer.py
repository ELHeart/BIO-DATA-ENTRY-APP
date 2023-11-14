# BIO-CAP is a python based Bio-data collection application currently under development.
# in this repository you will find detailed information about this application in the README file attached.
# Kindly assist with any errors or bugs you may find in the program.

print(" ")
print(" ")

# Introduction to the software.
print("***********************************************************")
print("Hello and Welcome to BIO-CAP. A Bio-data Entry Application.")
print("Kindly follow the instructions ad contact the System administrator if you need help")
print("***********************************************************")
print(" ")

# User consent
print("***********************************************************")
print("Enter 1 to begin bio-data entry or 0 to cancel.")
entry = int(input())

# Consent entry correction point and re-entry
while entry > 1:
    print(" Invalid input!!! Enter 1 or 0")
    entry = int(input())
print(" ")
print("***********************************************************")

# Bio-data Input begins if consent is given.
if entry == 1:
    print(" ")
    print("Bio-data entry begins")
    print("*******************************************")
    print("Enter your Name: ")
    name = input()
    print("Enter your Age: ")
    age = int(input())
    print("End of Bio-data Entry")

# Statement breaks program when user cancels
elif entry == 0:
    print("Bio-data entry was cancelled by the user!")
    print("Thank You")
