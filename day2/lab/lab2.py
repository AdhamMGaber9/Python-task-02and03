"""Q1 Write a function that accepts two arguments (length, start) to generate an array of a specific length filled with integer numbers increased by one from start."""

def generateAnArray (length,start):
    array = [start]
    for i in range (length):
        array.append(array[i]+1)
    return array

# print(generateAnArray(1,3))

"""Q2 write a function that takes a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both return "FizzBuzz"""

def divByFive (num):
    if num%3==0 and num%5==0:
        return "FizzBuzz"
    elif num%5==0:
        return "Buzz"
    elif num%3==0:
        return "Fizz"
    else:
        return "Not divisible"

# print(divByFive(7))

"""
Q3 Write a function which has an input of a string from user then it will return the same string reversed.
"""

def revString():
    text = input("please enter a string to reverse : ")
    return  text[::-1]

# print(revString())

"""Q4 Ask the user for his name then confirm that he has entered his name(not an empty string/integers). then proceed to ask him for his email and print all this data (Bonus) check if it is a valid email or not"""
import re
def validateInfo():
    while True:
        name = input("enter your name : ")
        print(name.isalpha())
        if name.isalpha():
            break
        else:
            print("please enter a valid name")
    while True:
        email= input("please enter your email : ")

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex,email):
            break
        else:
            print("pleas enter a vaild email : ")

# validateInfo()



"""Q5 Write a function that takes a string and prints the longest alphabetical ordered substring occurred For example, if
the string is 'abdulrahman' then the output is: Longest substring inalphabetical order is: abdu"""

def longestSubString(str):
    subString =  str[0]
    longest = ""
    for i in range(1,len(str)):
        if str[i]>=str[i-1]:
            subString+=str[i]
        else:
            if len(subString)>len(longest):
                longest=subString
            subString=str[i]

    if len(subString)> len(longest):
        longest=subString

    return  longest

# print(longestSubString("diaxzabcdefg"))

"""Q6 Write a program which repeatedly reads numbers until the user enters “done”."""

def readNums():
    nums=[]
    while True:
        num = input("pleas enter a number : ")
        if num=="done":
            break
        else:
            try:
                nums.append(int(num))
            except ValueError:
                print("enter a valid Number : ")

    if len(num)==0:
        print("no numbers were entered please try again")
    else:
        print(f"the total is {sum(nums)}")
        print(f"the count is {len(nums)}")
        print(f"the avg is {sum(nums)/len(nums)}")

# readNums()

"""Q7 Word guessing game (hangman)"""
