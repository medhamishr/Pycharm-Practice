from utils.utils1 import person2

obj = person2("sudhanshu", "kumar", 3456)
print(obj.yob1)

class person1:
    def __init__(self, name, surname, yob):
        self._name1 = name
        self.__surname1= surname
        self.yob1 = yob

sudh = person1("sudhanshu", "kumar", 1990)

print(sudh._name1)
print(sudh._person1__surname1)