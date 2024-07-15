print("""Question 1
      Divisible by 7 and Multiple of 5""")
for i in range(1500,2701):
    if i%5==0 and i%7==0:
        print(i)
print("""Question 2
      Conversion of Fahrenheit to Celcius and Celcius to Fahrenheit""")
def F_to_C(f):
    c=(f-32)/1.8
    return c
def C_to_F(c):
    f=c*1.8 + 32
    return f
f=float(input("Enter temperature in Fahrenheit: "))
c=float(input("Enter temperature in Celcius: "))
c2=F_to_C(f)
f2=C_to_F(c)
print(f"{c}°C is {f2} in Fahrenheit")
print(f"{f}°F is {c2:.1f} in Celsius")
print("""Question 3
      Random number between 1 to 9""")
import random
rand_no=random.randint(1,9)
value=int(input("Enter guess: "))
while rand_no!=value:
    value=int(input("Your guess is wrong, Enter again: "))
else:
    print("Well Guessed!")
print("""Question 4
      Diamond Pattern""")
c=1
for i in range(5):
    for j in range(c):
        print("*",end=" ")
    c=c+1
    print("")
c=c-2
for i in range(4):
    for j in range(c):
        print("*",end=" ")
    c=c-1
    print("")
print("""Question 5
      Reverse a word""")
word=input("Enter a word: ")
a=len(word)-1
rev=""
for i in range(len(word)):
    rev=rev+word[a]
    a=a-1
print("Reversed word is:",rev)
print("Another method to reverse a word is word[::-1]")
rev2=word[::-1]
print(rev2)
print("""Question 6
       Number of evens and odds""")

start=int(input("Enter start of series: "))
end=int(input("Enter end of series: "))
while start>end:
    print("Start is greater than End. Enter Again.")
    start=int(input("Enter start of series: "))
    end=int(input("Enter end of series: "))
even=0
odd=0
for i in range(start,end+1):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("Number of even numbers:",even,"Number of odd numbers:",odd)
print("""Question 7
       List Items with their Data Types""")
li=[1,2.3,"Muavia",None,True,1+2j,[1,2,3],{"r","s","t"},(1,5,9),{"name":"Mavi","age":22}]
for i in range(len(li)):
    print(f"{li[i]} has datatype {type(li[i])}")
print("""Question 8
       Print 0 to 6 except 3 and 6""")
for i in range(7):
    if(i==3 or i==6):
        continue
    print(i,end=" ")
print("")
print("""Question 9
      Fibonacci Series""")
a=0
b=1
c=a+b
print(a,b,end=" ")
while c<=50:
    print(c,end=" ")
    a=b
    b=c
    c=a+b
print("")
print("""Question with no number
      Series of 1 to 50 with fizz(multiple of 3) and buzz(multiple of 5)""")
for i in range(1,51):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)
print("""Question 10
      2D Array""") 
row=int(input("Enter Row Number: "))
col=int(input("Enter Column Number: "))
l=[]
for i in range(row):
    l.append([])
    for j in range(col):
        v=int(input("Enter a number: "))
        l[i].append(v)
print(l)
print("""Question 11
      Sequence of lines in lower case""") 
lines=[]
line=input("Enter a line: ")
while line!="":
    lines.append(line)
    line=input("Enter a line: ")
for i in lines:
    print(i.lower())
print("""Question 12
      Binary numbers divisible by 5""")
binary=input("Enter a series of 4 digit binary numbers with commas: ")
binary=binary.split(',')
decimals=[]
for i in binary:
    j=int(i,2)
    if j%5==0:
        decimals.append(i)
print(decimals)
print("""Question 13
      Number of digits and letters""")
newline=input("Enter a string: ")
letters=0
digits=0
for i in newline:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        letters=letters+1
    elif i>='0' and i<='9':
        digits=digits+1
    else:
        continue
print("Letters:",letters)
print("Digits:",digits)
print("""Question 14
      Validity of Password""")
ABC=0
abc=0
dig=0
char=0
password=input("""Enter a password with such specifications:
           At least 1 letter between [a-z] and 1 letter between [A-Z].
           At least 1 number between [0-9].
           At least 1 character from [$#@].
           Minimum length 6 characters.
           Maximum length 16 characters.""")
for i in password:
    if i>='a' and i<='z':
        abc=abc+1
    elif i>='A' and i<='Z':
        ABC=ABC+1
    elif i>='0' and i<='9':
        dig=dig+1
    elif i=='$' or i=='#' or i=='@':
        char=char+1
if(len(password)>=6 and len(password)<=16 and abc!=0 and ABC!=0 and dig!=0 and char!=0):
    print("Password is valid.")
else:
    print("Password is invalid.")


print("And Lab 3 ends here...")