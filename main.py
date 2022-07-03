from module1 import person
from module2 import employee
from utils.utils1 import concat_name


ravi1 = person("Ravi","Dubey", 1983)

#accessing protected variable
print(ravi1._name)

## accessing private variable of class with prefix of _ before class name
print(ravi1._person__surname)

#changing protected variable
ravi1._name = "Astha"
print(ravi1._name)

## changing private variable
ravi1._person__surname ="Trivedi"
print(ravi1._person__surname)

# ravi2 = module2.person2()
ravi3 = employee()
print(ravi3._name)
print(ravi3._employee__surname)
print(ravi3.year_of_birth)

print(concat_name(ravi3._name,ravi3._employee__surname))

