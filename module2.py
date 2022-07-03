#importing module1 in module2 and creating object in it

import module1
lika = module1.person("lika1","dubey",2019)
print(lika._name)
print(lika._person__surname)
print(lika.year_of_birth)


class person2:
    _name = "Ravi1"
    __surname = "Dubey1"
    year_of_birth = 1983

    def _age(self,current_year):
        return current_year - self.year_of_birth

    def __age(self,current_year):
        return current_year - self.year_of_birth


class employee(person2):
    _name = "Astha"
    __surname = "Trivedi"


ravi2 = person2()
ravi3 = employee()

print(ravi3._name)
print(ravi3._person2__surname)
print(ravi3._employee__surname)
print(ravi3.year_of_birth)
print(ravi3._age(2022))
print(ravi3._person2__age(2022))