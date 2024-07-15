class node:
    def __init__(self,data):
        self.setdata(data)
        self.next=None
    def setdata(self,data):
        self.data=data
    def getdata(self):
        return self.data
    def setnext(self,next):
        self.next=next
    def getnext(self):
        return self.next
    def showdata(self):
        print("Data is",self.data)
    
class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        ptr=node(data)
        if(self.isfull()):
            print("Stack is full.")
            exit(1)
        if(self.isempty()):
            self.top=ptr
        else:
            ptr.setnext(self.top)
            self.top=ptr
    def pop(self):
        if(self.isempty()):
            print("Stack is empty.")
            exit(1)
        else:
            temp_value=self.top.getdata()
            temp=self.top
            self.top=self.top.getnext()
            del temp
            return temp_value
    def topp(self):
        if(self.isempty()):
            print("Stack is empty.")
            exit(1)
        else:
            return self.top.getdata() 
    def isfull(self):
        ptr=node(1)
        if(ptr.getdata()==1):
            del ptr
            return False
        else:
            del ptr
            return True
    def isempty(self):
        return self.top==None
    def display(self):
        if(self.isempty()):
            print("Stack is empty.")
            exit(1)
        ptr=self.top
        while(ptr!=None):
            ptr.showdata()
            ptr=ptr.getnext()
    def toppp(self):
        return self.top

class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        ptr=node(data)
        if(self.isfull()):
            print("Queue is full.")
            exit(1)
        if(self.isempty()):
            self.front=ptr
            self.rear=ptr
        else:
            self.rear.setnext(ptr)
            self.rear=ptr
    def dequeue(self):
        if(self.isempty()):
            print("Queue is empty.")
            exit(1)
        else:
            temp_value=self.front.getdata()
            temp=self.front
            self.front=self.front.getnext()
            del temp
            return temp_value
    def start(self):
        if(self.isempty()):
            print("Queue is empty.")
            exit(1)
        else:
            return self.front.getdata() 
    def isfull(self):
        ptr=node(1)
        if(ptr.getdata()==1):
            del ptr
            return False
        else:
            del ptr
            return True
    def isempty(self):
        return self.front==None 
    def display(self):
        if(self.isempty()):
            print("Queue is empty.")
            exit(1)
        ptr=self.front
        while(ptr!=None):
            ptr.showdata()
            ptr=ptr.getnext()
    def fromtt(self):
        return self.front


s1=stack()
q1=queue()
val=int(input("How many values you want to enter in stack and queue: "))
print("Enter values 1 by 1")
for i in range(val):
    v=int(input())
    s1.push(v)
    q1.enqueue(v)
s1.pop()
q1.dequeue()
s1.push(11)
q1.enqueue(11)
print("After popping dequeuing 1 value from both stack and queue and applysing push(11) and enqueue(11) on stack and queue,")
print("Values in Stack are:")
s1.display()
print("Values in Queue are:")
q1.display()

print("""Now Let's go to the 3rd question of the lab
         THE BINARY SEARCH""")
print("Enter values in the list/array until -1 comes")
l1=[]
i=int(input())
while i!=-1:
    l1.append(i)
    i=int(input())
    
l1.sort()
print("Sorted list is: ")
print(l1)

v1=int(input("Enter value you want to search: "))
loc=-1
start=0
end=len(l1)-1
while(start<end):
    mid=int((start+end)/2)
    if v1<l1[mid]:
        end=mid-1
    elif v1>l1[mid]:
        start=mid+1
    elif v1==l1[mid]:
        loc=mid
        break
    
if loc==-1:
    print("Value not found")
else:
    print(f"Value is found at index {mid}")
