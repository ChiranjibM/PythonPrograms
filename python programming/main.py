'''
#this is py program

import cv2
import math

print("hi python\n")
print(math.gcd(3,6))


multi
line 
comments


print(5+4)
age=8
if(age<18):
    print("hello")
print("end")

a = 34
b = a
print (b)
print(a+4)
typeA = type(a)
print(typeA)

e="31"
e="wee"
e=float(e)
e=int(e)
print(e+2)

name="   this IS gOOd"
name1="Chandan"
name2="Xman"
print(name.strip())
print(name[2:6])
print(len(name))
var=name.lower()
var=name.replace(" ", "\n")
print(var)
print("this is {} and {}".format(name1, name2))
temp = f"they are {name1} and {name2}"
print(temp)

list, tupple, set, disctionary

lst = [21,5,667,788,44]
print(type(lst))
lst[2]=333
lst.append(45)
#lst.insert(0,100)
#lst.remove(333)
#lst.pop()
#del lst[0]
#lst.clear()
var = lst[2]
print(var)
print(lst)

a = ("abc", "cde", "xyz")
var = a
#a[0]="ddd" not possible
var = type(a)
print(var)

set1 = {323,3,3,4,5,56,767,32}
#set1.discard(33321) will not throw error if that element not present
set1.remove(3)
print(set1)

mydictionary = {
    "name": "Chandan",
    "laptop": "hp",
    "mobile": 999977888,
    "profession": "IT"
}
print(mydictionary)
print(mydictionary.keys())
mydictionary["laptop"]="dell"
mydictionary.pop("mobile")
print(mydictionary["laptop"])
print(mydictionary)

age = input("Enter age\n")
age = int(age)

if(age>18):
    print("ready to drive")
elif(age==18):
    print("wait for an year")
else:
    print("not ready")

#for i in range(0,100):
#    print(i)
li = [1,445,"sas"]
for item in li:
    print(item)
i=0
while(i<10):
    i=i+1
    if i==6:
        continue
    #   break
    print(i+1)

def sum(a,b):
    c=a+b
    return c

print(sum(44,55))

def greet(name):
    print("good day!"name)
    return;
greet(chandan)
'''
class Employee:
#constructor    
def_init_(self,gname, gsalary):
    self.name = name
    self.salary = salary

harry = Employee("xxx",44)
print(harry.name)
print(harry.salary)
