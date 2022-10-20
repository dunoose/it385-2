from selectors import EpollSelector


testPassword = "goodPassword007!"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upperCaseTest = False
lowercase = "acbdefghijklmnopqrstuvwxyz"
lowerCaseTest = False
lengthTest = False
number = "0123456789"
testNumber = False
special = "!@#$%^*()_<>?"
specialTest = False

print("Testing for:", testPassword)

if 8 <= len(testPassword):
    print("Your password PASSED the length Test")
for a in testPassword:
    if a in upperCase:
        upperCaseTest = True
    if upperCaseTest == True:
        print("Your Password PASSED the Uppercase Test")
        break
    else:
        print("Your Password FAILED the Uppercase Test")

for i in testPassword:
    if i in lowercase:
        lowerCaseTest = True
    if lowerCaseTest == True:
        print("Your Password PASSED the LowerCase Test")
        break
    else:
        print("Your Password FAILED the Special Test")

for n in testPassword:
    if n in number:
        testNumber = True
    if testNumber == True:
        print("Your Password PASSED the Number Test")
        break
    else:
        print("Your Password FAILED the Number Test")