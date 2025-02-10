def addition(num1,num2) :
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2



print("please select the operations -/n"
      "1. addition /n"
      "2.subtract/n"
      "3. multiply/n"
      "4. division/n ")

select = int(input("select operations form 1, 2 ,3,4 :"))

number1 = int(input("enter the first number:"))
number2 = int(input("enter the second number:"))

if select == 1:
    print(number1,"+",number2,"=",
          addition(number1,number2))
elif select == 2 :
    print(number1,"-",number2,"=",
          subtract(number1,number2))
elif select == 3 :
    print(number1,"*",number2,"=",
          multiply(number1,number2))
elif select == 4 :
    print(number1,"/",number2,"=",
          division(number1,number2))
else :
    print("invalid input")

