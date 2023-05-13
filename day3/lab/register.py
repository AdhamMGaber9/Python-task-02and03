import json
from fileHandlers import *
from helpers.valid import *
import uuid

# def write_json(new_data, filename='users.txt'):
#         email= new_data["email"]
#         userdata = ",".join(new_data.values())
#
#         userdata = userdata + "\n"
#
#         try:
#                 readfile = open(filename)
#         except:
#                 print("File Doesnt Exit")
#         else:
#                 # read data from file
#                 data = readfile.readlines()
#                 users = []
#
#                 for i in data:
#                         users.append(i.strip("\n"))
#                 # to check if user email exits or not
#                 for user in users:
#                         userdetails = user.split(",")
#                         print(user)
#                         if userdetails[3] == email:
#                                 # print(f"userdetails : {userdetails}")
#                                 print("Email Already Exits")
#                                 readfile.close()
#                                 return
#                 else:
#                         readfile.close()
#                         try:
#                                 file = open(filename, "a")
#                         except:
#                                 print("File Doesnt Exit")
#                         else:
#                                 file.write(userdata)
#                                 file.close()
#                                 print("Registration Done Successfully")

def register():
        hello()
        userId = uuid.uuid4().hex
        firstName = isAlpha(input("please enter your first name : "))
        lastName = isAlpha(input("please enter your last name : "))
        # email = isValidEmail(input("please enter your email : "))
        password = validPassword(input("please enter your password : "))
        mobilePhone= validMobilePhone(input("please enter your mobile phone"))
        # print(userId,firstName,lastName,email,password)

        users = readFromFile('users.txt')
        while True:
                email = isValidEmail(input("please enter your email : "))
                exists= False
                for user in users:
                        userdetails = user.split(",")
                        print(user)
                        if userdetails[3] == email:
                                # print(f"userdetails : {userdetails}")
                                print("Email Already Exits")
                                exists=True
                                break
                if exists == False:
                        break

        data ={
                "userId":userId,
                "firtName":firstName,
                "lastName":lastName,
                "email":email,
                "password":password,
                "mobilePhone":mobilePhone,
        }
        writeIntoFile('./users.txt',data)



# register()








# try:
        # with open(filename, 'a') as outfile:
        #         outfile.write(json.dumps(new_data,indent=4))
        #         outfile.write(",")
        #         outfile.close()
        #         with open(filename) as data_file:
        #                 old_data = json.load(data_file)
        #         print(old_data)
        #         old_data.append(new_data)
        #         print(old_data)
        #         with open(filename, "w") as write_file:
        #                 json.dump(old_data, write_file,indent=4)
        # except:
        #         with open(filename, "w") as write_file:
        #                 json.dump(new_data, write_file, indent=4)
#
from  helpers import *
# class User:
#     def __int__(self,firstName,lastName,email,password,mobilePhone):
#         print("object is being created")
#         self.firstName =firstName
#         self.lastName = lastName
#         self.email = email
#         self.password = password
#         self.mobilePhone = mobilePhone
#
#     # def register(self):
#     #     valid.hello()
#     #     self.firstName = valid.isAlpha(input("please enter your first name : "))
#     #     self.lastName = valid.isAlpha(input("please enter your last name : "))
#     #     self.email = valid.isValidEmail(input("please enter your email : "))
#     #     self.password = valid.validPassword(input("please enter your password : "))
#     #     print(self.firstName, self.lastName, self.email, self.password)
#     def register(self):
#         valid.hello()
#         firstName = valid.isAlpha(input("please enter your first name : "))
#         lastName = valid.isAlpha(input("please enter your last name : "))
#         email = valid.isValidEmail(input("please enter your email : "))
#         password = valid.validPassword(input("please enter your password : "))
#         print(firstName, lastName, email, password)