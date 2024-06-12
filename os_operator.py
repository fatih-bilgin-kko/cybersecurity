def os_operator(funcname):
    import os
    if funcname=="name":
        return os.name
    elif funcname=="getcwd":
        return os.getcwd()
    elif funcname=="cd":
        return os.chdir(path=input())
    elif funcname=="mkdir":
        if int(input())>1:
            return os.mkdir(path=input())
        else:
           return os.makedirs(path=input())
    elif funcname=="rmdir":
        if int(input())>1:
            return os.rmdir(path=input())
        else:
            return os.removedirs(path=input())
    elif funcname=="listdir":
        return os.listdir(path=input())
    elif funcname=="find":
        file=input()
        if os.path.exists(file):
            return os.path.abspath(file)
    elif funcname=="command":
        while True:
            command=input("Enter your command: ")
            if command!="END":
                os.system(command)
            else:
                break
while True:
    print(os_operator(input()))


