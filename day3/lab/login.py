from helpers.valid import *
def login():
    email = isValidEmail(input("please enter your email : "))
    password = validLoginPassword(input("please enter your password : "))
    readfile = open("users.txt")
    data = readfile.readlines()
    users = []
    for i in data:
        users.append(i.strip("\n"))
    for user in users:
        userdetails = user.split(",")
        if userdetails[3] == email and userdetails[4] == password:
            print("Logged in Successfully")
            # mainMenu.projectmenu(email)
            readfile.close()
            break
    else:
        print("User Doesnt Exit")
        login()
    print(userdetails[0])
    return userdetails[0]

# login()