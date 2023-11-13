# Introduction to the software
print("Hello and welcome to the Bio-data Entry App.")
print("Kindly follow the instructions ad contact the System administrator if you need help")

# User consent
print("Enter 1 to begin bio-data entry or 0 to cancel.")
entry = int(input())
# Consent entry correction point and re-entry
while entry != 1 or 0:
    print("Enter either 1 to begin or 0 to cancel")
    entry = int(input())

# Bio-data Input begins
if entry == 1:
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
