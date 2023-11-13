# Introduction to the software
print("Hello and welcome to the Bio-data Entry App.")
print("Kindly follow the instructions ad contact the System administrator if you need help")

# fhjfhg
print("Bio-data entry begins now. Enter 1 to begin or 0 to cancel.")
entry = int(input())
while entry != 1 or 0:
    print("Enter either 1 to begin or 0 to cancel")
    entry = int(input())

if entry == 1:
    print(" ")
    print("*******************************************")
    print("Enter your Name: ")
    name = input()
    print("Enter your Age: ")
    age = int(input())
    print("End of Bio-data Entry")
elif entry == 0:
    print("Bio-data entry was cancelled by the user!")
    print("Thank You")
