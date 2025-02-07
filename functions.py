# built-in functions/standard library functions

y = max(67,44,57,24,78)
print("the maximum value is",y)

x = min(34,32,65)
print("the minimum value is ",x)

#user-defined functions
def name() :
    print("tonny")
name()   #calling a function

def multiply() :
    x = 10
    y = 2
    print(x * y)
multiply()

# parameter/variable and arguments/value
def add(a,b):
    print(a +b)
add(1,4)
add(20,45)

def employee(name,gender,position,salary,age):
    print(name,gender,position,salary,age)
employee("tonny","male","CEO","560000","36")
employee("mark","male","manager","40000","34")
employee("ken","male","secretary","28000","29")


# a program that displays details of 5 students
#user defined function with the parameter and argument
#fullname,age,course,gender

def student(fullname ,age,course,gender):
    print(fullname,age,course,gender)
student("richard Juma",17,"MIT","male")
student("leah mwikali",20,"cybersecurity","female")
student("mark mwenda",22,"data science","male")
student("michael thusi",20,"actuarial","male")
student("riko owens",25,"aviation","male")