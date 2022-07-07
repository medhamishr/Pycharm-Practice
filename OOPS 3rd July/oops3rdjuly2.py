import oops3rdjuly
print(oops3rdjuly)

obj3= oops3rdjuly.person1("sudhanshu", "kumar", 1994)
print(obj3.yob1)
print(obj3._name1)
print(obj3._person1__surname1)
class person:

    _name = "sudh"
    __surname = "kumar"
    yob =1990
    def _age(self, currentyear):
        return currentyear - self.yob
    def __age1(self, currentyear):
        return currentyear - self.yob

obj= person()
print(obj._age(2022))
print(obj._person__age1(2022))

class employee(person):
   _name = "sudhanshu"
   __surname = "singh"
   yob = 1991

obj1= employee()
print(obj1._age(2022))
print(obj1._person__age1(2022))
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._person__surname)

