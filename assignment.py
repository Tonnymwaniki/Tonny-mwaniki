#a program to check whether year is a leap year or not

#a program to check whether a letter is a consonant or a vowel

year = 2024

if (year % 400 ==0) and (year % 100 ==0):
    print("is a leap year",year)
elif (year % 4==0) and (year % 100 != 0) :
    print("is a leap year",year)
else :
    print("is not a leap year",year)


letter = "a"


if letter =="a"or letter == "e" or letter == "i"or letter == "o" or letter == "u" :
    print("is a vowel")
else:
    print("is a consonant")

