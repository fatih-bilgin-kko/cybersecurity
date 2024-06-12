#file_name=input("filename:")
with open("D:/yazılım bilgisayar/siber güvenlik/kodlar/textfile.txt","r") as file: 
    data=file.readlines()
    with open("D:/yazılım bilgisayar/siber güvenlik/kodlar/copy.txt","w") as file2:
        file2.writelines(data)
        print("file copied")

