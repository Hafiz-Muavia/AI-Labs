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
    
class graph:
    def __init__(self):
        self.graph={}
    def addnode(self, node):
        if node not in self.graph:
            self.graph[node]=[]
    def addedge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
    def displaygraph(self):
        for node in self.graph:
            print(node, self.graph[node])
    def BFS(self,s):
        visited=[]
        q1=queue()
        q1.enqueue(s)
        while not q1.isempty():
            q=q1.dequeue()
            if q not in visited:
                print(q)
                if q=='G':
                    print("Search Completed. Goal achieved.")
                    break
                visited.append(q)
                for i in self.graph[q]:
                    q1.enqueue(i)
        
#Task 1: Graph implementation

g=graph()
g.addnode(0)
g.addnode(1)
g.addnode(2)
g.addnode(3)
g.addnode(4)

g.addedge(0,1)
g.addedge(0,4)
g.addedge(2,1)
g.addedge(3,1)
g.addedge(4,1)
g.addedge(2,3)
g.addedge(3,4)

g.displaygraph()

#Task 2: BFS Implementation

print("Task 2, Graph 2")
g1=graph()
g1.addnode('A')
g1.addnode('B')
g1.addnode('C')
g1.addnode('D')
g1.addnode('E')
g1.addnode('F')
g1.addnode('G')
g1.addnode('H')
g1.addnode('I')
g1.addnode('J')
g1.addnode('K')
g1.addnode('L')
g1.addnode('M')
g1.addnode('N')

g1.addedge('A','B')
g1.addedge('A','F')
g1.addedge('A','D')
g1.addedge('A','E')
g1.addedge('K','B')
g1.addedge('J','B')
g1.addedge('K','M')
g1.addedge('K','N')
g1.addedge('D','G')
g1.addedge('E','C')
g1.addedge('E','H')
g1.addedge('E','I')
g1.addedge('I','L')

g1.displaygraph()

print("BFS Implementation")
g1.BFS('A')





#Task 3: Priority Queue
n=int(input("How many values you want to enter in priority queue: "))
l=[]
print("Add values.")
for i in range(n):
    j=int(input())
    l.append(j)
l.sort()
priorityqueue=queue()
for i in l:
    priorityqueue.enqueue(i)
print("Data in Priority Queue")
priorityqueue.display()


