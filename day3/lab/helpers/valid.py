import re
from datetime import datetime
def isAlpha(str):
    while True:
        if str.isalpha():
            return  str
        else:
            str = input("please enter a valid string : ")

def isNum(str):
    while True:
        if str.isdigit():
            return  str
        else:
            str = input("please enter a valid digit : ")


def isValidEmail(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    while True:
        if re.fullmatch(regex,email):
            return email
        else:
            email = input("please enter a valid email : ")


def validPassword(password):
    confirmPassword = input("please enter your password again : " )
    while True:
        if  password== confirmPassword and len(password) >8 :
            return password
        else:
            print("your password must be identical and greater than 8 charcaters")
            password= input("please enter your password  : ")
            confirmPassword= input("please enter your password again : " )

def validLoginPassword(password):
    while True:
        if  len(password) >8 :
            return password
        else:
            print("your password must be greater than 8 charcaters")
            password= input("please enter your password  : ")
            # confirmPassword= input("please enter your password again : " )
def validMobilePhone(phone):
    regex = re.compile("01[0-2]\d{1,8}$")
    while True:
        if re.fullmatch(regex,phone) and len(phone) == 11:
            return phone
        else:
            print("please enter a valid mobile phone number : ")
            phone = input("please enter your mobile phone number  : ")

def isValidDate(str):
    res = False
    while True:
        try:
            res = bool(datetime.strptime(str, "%d-%m-%Y"))
        except ValueError:
            print(ValueError)
        if res == True:
            break
        else:
            print("please enter a valid date format : ")
            str = input("please enter your project start date (dd-mm-yyyy) : ")
    print(str)
    return str

def hello():
    print("hello")