import random
class Cypher():   
    def __init__(self,message) -> None:
        self.message=message
        self.alphabets={
            "EN": ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z'],
            "TR":['A','a','B','b','C','c','Ç','ç','D','d','E','e','F','f','G','g','Ğ','ğ','H','h','İ','i','I','ı','J','j','K','k','L','l','M','m','N','n','O','o','Ö','ö','P','p','R','r','S','s','Ş','ş','T','t','U','u','Ü','ü','V','v','Y','y','Z','z']
            }
    def ROTn(self,alp_code,n):
        alp=self.alphabets[alp_code]
        cyp_mes=list(map(lambda x:alp[alp.index(x)+2*n],[c for c in self.message]))
        return cyp_mes
    def rev_ROTn(self,alp_code,n):
        alp=self.alphabets[alp_code]
        cyp_mes=list(map(lambda x:alp[alp.index(x)-2*n],[c for c in self.message]))
        return cyp_mes
    def key_maker(characters):
        
        chars=[]
        for n in range(len(characters)):
            chars.append(characters[n])
        cyp_dict={}  
        for i in range(len(characters)):
            c=random.choice(chars)
            cyp_dict[characters[i]]=c
            chars.remove(c)
        return cyp_dict
    def decypher(self,key):
        decyp_mes=""
        for i in [c for c in self.message]:
            try:
                decyp_mes+=key[i]
            except KeyError:
                decyp_mes+=i
        return decyp_mes
    def cypher(self,key):
        cyp_mes=""
        for i in [c for c in self.message]:
            try:
                cyp_mes+=key[i]
            except KeyError:
                cyp_mes+=i
        return cyp_mes
    def file_cypher(file_path,key):
        with open(file_path,"r+") as file:
            cyp_mes=Cypher.cypher(file.read(),key)
            file.write(cyp_mes)
    def file_decypher(file_path,key):
        with open(file_path,"r+") as file:
            decyp_mes=Cypher.decypher(file.read(),key)
            file.write(decyp_mes)
class Password:
    def __init__(self,length,alp_code,spesigns):
        self.length=length
        self.alphabets={
            "EN": ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z'],
            "TR":['A','a','B','b','C','c','Ç','ç','D','d','E','e','F','f','G','g','Ğ','ğ','H','h','İ','i','I','ı','J','j','K','k','L','l','M','m','N','n','O','o','Ö','ö','P','p','R','r','S','s','Ş','ş','T','t','U','u','Ü','ü','V','v','Y','y','Z','z']
            }
        self.password=""
        self.lower=list(filter(lambda x:x.islower,self.alphabets[alp_code]))
        self.lower_upper=list(filter(lambda x:x.isalpha,self.alphabets[alp_code]))
        self.alnum=list(filter(lambda x:x.isalnum,self.alphabets[alp_code]))
        self.alnum_spesign=self.alnum.append(spesigns)

    def PIN(self): 
        for i in range(self.length):
            self.password +=random.randint(0,9)
    def Text(self):
        if input()=="1":
            for i in range(self.length):
                self.password+=random.choice(self.lower)
        elif input()=="2":
            for i in range(self.length):
                self.password+=random.choice(self.lower_upper)
        elif input()=="3":
            for i in range(self.length):
                self.password+=random.choice(self.alnum)
        elif input()=="4":
            for i in range(self.length):
                self.password+=random.choice(self.alnum_spesign)
        return self.password
    def password_maker(func_name,length):
        if func_name=="PIN":return Password.PIN(length)
        elif func_name=="Text":return Password.Text(length)
