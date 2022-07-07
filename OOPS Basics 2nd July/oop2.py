class person:

    def __init__(sudh, name,surname, eamilid, yearofbirth): #sudh is a pointer
        sudh.name= name
        sudh.surname = surname
        sudh.eamilid =  eamilid
        sudh.yearofbirth = yearofbirth

    def __init__(sudh, name,surname): #sudh is a pointer
        sudh.name= name
        sudh.surname = surname
        sudh.eamilid =  eamilid
        sudh.yearofbirth = yearofbirth

    def age(self, currentyear):
        return currentyear-sudh.yearofbirth

anuj_var = person("anuj", "bhandari", "anuj@gmail.com", 1994)
sudh = person("sudhanshu", "kumar", "sudhanshu@gmail.com", 2345)
medha= person ("medha", "mishra","medhamishra@gmail.com", 1994)
print(sudh.age(2022))

s= "sudh"
s.upper()