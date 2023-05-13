from login import login
from register import register
from project import *

def projectMenu(userId):
    while True:
        print("please enter your choice : ")
        print("1- Create Project ")
        print("2- Get All Projects ")
        print("3- Edit Project ")
        print("4- delete Project ")
        print("5- Logout")
        choice = int(input("Your choice : "))
        if choice == 1:
            createPorject(userId)
        if choice==2:
            getAllProjects()
        if choice == 3:
            editProject(userId)
        if choice == 4:
            print(userId)
            deleteProject(userId)
        if choice==5:
            mainMenu()
def mainMenu():
    while True:
        print("welcome to crowd funding")
        print("please enter your choice : ")
        print("1- Register ")
        print("2- Login ")
        print("3- exit ")
        choice = int(input("Your choice : "))
        if choice==1:
            register()
        elif choice==2:
            userId=login()
            print(userId)
            if userId:
                projectMenu(userId)
        elif choice==3:
            exit()
        else:
            print("Wrong Choice")

mainMenu()
