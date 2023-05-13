def readFromFile(filename):
    try:
        fileObj = open(filename, 'r')
        pass
    except Exception as e:
        print(e)
    else:
        data = fileObj.readlines()
        fileObj.close()
        return data

def writeIntoFile(filename, data):
    userdata = ",".join(data.values())

    userdata = userdata + "\n"
    print(userdata)
    try:
        fileObj = open(filename, 'a')
        pass
    except Exception as e:
        print(e)
    else:
        fileObj.writelines(userdata)
        fileObj.close()
        print("Data Added Successfully")

def overwrite(filenane, data):
    try:
        fileObj = open(filenane, 'w')
        pass
    except Exception as e:
        print(e)
    else:
        fileObj.writelines(data)
        fileObj.close()