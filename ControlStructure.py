#single if
# age = int(input("Enter your age"))

# if age>=18:
#     print("Adult")
# else:
#     print("Under Age")


firstNumber = int(input("Enter the first Number"))
secondNumber = int(input("Enter second Number"))
thirdNumber = int(input("Enter the third Number"))

if firstNumber>secondNumber and firstNumber>thirdNumber:
    print(firstNumber, "is the greatest of all")
elif secondNumber>firstNumber and secondNumber>thirdNumber:
    print(secondNumber, "is the greatet of all")
    
elif thirdNumber>firstNumber and thirdNumber>secondNumber:
     print(thirdNumber, "is the greatest of all")



    