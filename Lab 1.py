#print statement

print("Hello, Welcome to Muavia's Lab-1")

#input statement

name=input("I told you my name. Let's tells yours too to go further: ")

#2 statements in same line 

print("So, I'm Muavia");print("And you are",name)

#indentation with if statement

gender=input("Now tell me your Gender. Press G for girl and B for boy: ")
if gender=='B':
    print("So you are a boy")
elif gender=='G':
    print("So you are a girl")
else:
    print("Wrong choice. Anyways Let's go further")

#use type() function

print("Type of", name,"is",type(name))
print("And that of",gender,"is",type(gender))
print("Type of None is",type(None))
print("And that of True is",type(True))
print("And finally type of 1+2j is",type(1+2j))
print("Type of",1,"is",type(1))
print("And that of",2.3,"is",type(2.3))

#Strings

print("Muavia in double quotations")
print('Muavia in single quotes')
print("Muavis's Birthday is in April")
print('But he has "Something Important" to do')

#Special Characters

print("You know we can go on next line in same statement with \\n Let's try it.\nOh we are on next line.")
print("Let's try \\t.\tAfter using \\t we are here.")
print("Same is true for \\,\',\"")

#String indices

str="Muavia"
print(str+"\'s 2nd index is",str[2],"and its -3rd index is",str[-3])

#List

print("Let's make a list of fav colors with ratings in next index of names")
li=["Pink",5,"Purple",4.5,"Grey",4.2,"Black",4]

print(li)

#List Indices

print(li[0],"color has rating",li[1])
print("and color",li[-2],"has rating",li[-1])

#List slice

li2=li[0:3]
print("Sliced list from index 0 to 2 is" ,li2)
print("Sliced list from 2 to -2 is",li[2:-1])
print("Copy of original list with slicing is",li[:])

print("And here Lab1 ends.\nThank you!")



