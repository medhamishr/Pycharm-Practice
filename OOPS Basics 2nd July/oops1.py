class person:

    def __init__(self, name,surname, eamilid, yearofbirth):
        self.name= name
        self.surname = surname
        self.eamilid =  eamilid
        self.yearofbirth = yearofbirth

anuj_var = person("anuj", "bhandari", "anuj@gmail.com", 1994)
sudh = person("sudhanshu", "kumar", "sudhanshu@gmail.com", 2345)
medha= person ("medha", "mishra","medhamishra@gmail.com", 1994)
print(anuj_var.name)
print(sudh.surname)
print(medha.eamilid)
print(type(sudh))
