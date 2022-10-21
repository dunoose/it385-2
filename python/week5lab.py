from selectors import EpollSelector

#Variables
testPassword = input("Choose a Password.")
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upperCaseTest = False
lowercase = "acbdefghijklmnopqrstuvwxyz"
lowerCaseTest = False
lengthTest = False
number = "0123456789"
testNumber = False
special = "!@#$%^*()_<>?"
specialTest = False

#Lets user know what it is testing for.
print("Testing for:", testPassword)

#Tests for Password Length must be greater than 8 Characters
if 8 <= len(testPassword):
    print("Your password PASSED the length Test")

#Tests for Capital Characters
for a in testPassword:
    if a in upperCase:
        upperCaseTest = True
    if upperCaseTest == True:
        print("Your Password PASSED the Uppercase Test")
        break
    else:
        print("Your Password FAILED the Uppercase Test")

#Tests for lowercase characters
for i in testPassword:
    if i in lowercase:
        lowerCaseTest = True
    if lowerCaseTest == True:
        print("Your Password PASSED the LowerCase Test")
        break
    else:
        print("Your Password FAILED the Special Test")

#Tests for Special Characters.
for c in testPassword:
    if c in special:
        specialTest = True
    if specialTest == True:
        print("Your Password PASSED the Special Test")
        break
    else:
        print("Your Password FAILED the Special Test")

#Tests for intergers
for n in testPassword:
    if n in number:
        testNumber = True
    if testNumber == True:
        print("Your Password PASSED the Number Test")
        break
    else:
        print("Your Password FAILED the Number Test")

#Lets the user know if the password met all the conditions or not.
if upperCaseTest == True and lowerCaseTest == True and specialTest == True and testNumber == True:
    print("Your password passed all the tests.")
else:
    print("Your password did not match all the conditions.")