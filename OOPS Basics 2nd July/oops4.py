class person:
    def age(self, currentyear, yearofbirth):
        return currentyear - yearofbirth

    def email(self, emailid):
        print ("take and mail ud from person and print", emailid)

    def askname(self):
        name=input("tell me your name")
        return  name
    def askdoubt(self):
        dob=input("tell me your dob")
        return dob

sudh = person()
medha = person()
jayant =  person()
krish = person()
gargi = person()

sudh.email("sudha@ineuron.ai")
print(sudh.askname())
krish.age(2022)