from helpers.valid import *
from fileHandlers import *
import uuid
import time

def createPorject(userId):
    projectId = uuid.uuid4().hex
    title = isAlpha(input("please enter your project title : "))
    details = isAlpha(input("please enter your project details : "))
    totalTarget = isNum(input("please enter your project total target : "))
    startTime = isValidDate(input("please enter your project start date (dd-mm-yyyy) : "))
    endTime = isValidDate(input("please enter your project end date (dd-mm-yyyy) : "))
    startValid = time.strptime(startTime, "%d-%m-%Y")
    endValid = time.strptime(endTime, "%d-%m-%Y")
    data = {
        "userId": userId,
        "projectId": projectId,
        "title": title,
        "details": details,
        "totalTarget": totalTarget,
        "startTime": startTime,
        "endTime": endTime,
    }
    while True:
        if startValid < endValid:
            writeIntoFile("./projects.txt", data)
            break
        else:
            print("Invalid Start and end date")
            startTime = isValidDate(input("please enter your project start date (dd-mm-yyyy) : "))
            endTime = isValidDate(input("please enter your project end date (dd-mm-yyyy) : "))
            startValid = time.strptime(startTime, "%d-%m-%Y")
            endValid = time.strptime(endTime, "%d-%m-%Y")
            data = {
                "userId": userId,
                "projectId": projectId,
                "title": title,
                "details": details,
                "totalTarget": totalTarget,
                "startTime": startTime,
                "endTime": endTime,
            }

def getAllProjects():
    projects = readFromFile("./projects.txt")
    print(len(projects))
    i=0
    while i< len(projects):
        print(projects[i])
        i+=1


def editProject(userId):
    projectId = input("enter project id to update: ")
    projects = readFromFile("./projects.txt")
    oldData=""
    for project in projects:
        projectDetails = project.split(",")
        # print(projectDetails)
        if projectDetails[0] == userId and projectDetails[1]==projectId:
            oldData = projectDetails
            projects.remove(project)
            break
    print(oldData)
    if oldData=="":
        print("wrong id or not authorized")
    else:
        print("enter what to edit")
        print("1- Edit Title")
        print("2- Edit Details ")
        print("3- Edit Total Target")
        choice = int(input("enter your choice: "))
        while True:
            if choice == 1:
                title = isAlpha(input("please enter your new project title : "))
                newData = f"{userId},{projectId},{title},{oldData[3]},{oldData[4]},{oldData[5]},{oldData[6]}"
                break
            elif choice == 2:
                details = isAlpha(input("please enter your project details : "))
                newData = f"{userId},{projectId},{oldData[2]},{details},{oldData[4]},{oldData[5]},{oldData[6]}"
                break
            elif choice == 3:
                totalTarget = isNum(input("please enter your project total target : "))
                newData = f"{oldData[0]},{oldData[1]},{oldData[2]},{oldData[3]},{totalTarget},{oldData[5]},{oldData[6]}"
                break
            else:
                print("invalid choice")
                print("enter what to edit")
                print("1- Edit Title")
                print("2- Edit Details ")
                print("3- Edit Total Target")
                choice = input("enter your choice: ")
        projects.append(newData)
        overwrite("./projects.txt", projects)



def deleteProject(userId):
    projectId = input("enter project id to delete: ")
    projects = readFromFile("./projects.txt")
    isFound =False
    for project in projects:
        projectDetails = project.split(",")
        # print(projectDetails[0])
        # print(projectDetails[1])
        if projectDetails[0] == userId and projectDetails[1] == projectId:
            isFound=True
            projects.remove(project)
            overwrite("./projects.txt", projects)
            print("Deleted!!")
            break
    if isFound==False:
        print("wrong id or not authorized")