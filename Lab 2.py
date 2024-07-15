print("Hello, Welcome to Muavia's Lab-2")

#while loop

print("Let's draw the table of 11 with while loop.")
i=1
while i<=10:
    print(11,"*",i,"=",11*i)
    i=i+1

#single statement with while loop

while i==11: print("i is 11 now");i=i+1

#for loop

print("Let's see how for loop works with a list. List is here: ")
li=["red", "pink", "purple"]
print(li)
for i in li:
    print(i)

#String with for loop 

print("And if we want each character from list then:")
for i in li:
    print(i,"has following characters")
    for j in i:
        print(j)

#Iteration with indices

print("Let's print for loop with range element")
for i in range(len(li)):
    print(li[i])
   
#break and continue statement

print("Let's do break and continue statements. Continue Muavia on a, Break Muavia on i, Otherwise print")
for i in "Muavia":
    if i=='a':
        continue
    if i=='i':
        break
    print(i)

#Functions

def myfunc():
    print("That's my very first FUNCTION")
 
print("Let's call our first function")
myfunc()

#Parameterized Function

def myfunc(a):
    print("Here is a parameterized function with parameter",a)

print("Let's call PARAMETERIZED FUNCTION")
myfunc("Mavi")

#Default Parameter value Function

def fun(a="Pakistan"):
    print("I live in",a)

print("Let's call DEFAULT VALUE PARAMETERIZED FUNCTION")
fun()
fun("Thailand")

#Passing List as parameter

def list_func(a):
    for i in a:
        print(i)

print("Let's call a function that takes a list as a parameter")
list_func(li)

#Functions with return Statement

def func(a):
    return 10-a

print("Let's call a function that returns a parameter")
a=func(3)
print(a)

#Function calling with keyword arguments

def func(a,b,c):
    print(a,"won")
    print(b,"is second")
    print(c,"is third")

print("Let's call a function with keyword arguments")
func(b="Mahi",c="Hui",a="Muavia")

#Class and Objects

class MyClass():
    x=5

p1=MyClass()
print(p1.x)

#_init_ function

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
p2=Person("Muavia",22)
print(p2.name,p2.age)

#Methods

class new():
    def new1(self):
        print("Hello Guys")

p3=new()
p3.new1()

class Student():
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def info(self):
        print(self.name,"with age",self.age,"gained",self.marks,"marks")
        #Another method of this thing
        print(f"{self.name} with age {self.age} gained {self.marks} marks")

p4=Student("Mahi",19,100)
p4.info()

print("Lab 2 Completed")
