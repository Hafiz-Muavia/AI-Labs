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
    def DFS(self,s):
        visited=[]
        s1=stack()
        s1.push(s)
        result=[]
        while not s1.isempty():
            q=s1.pop()
            if q not in visited:
                visited.append(q)
                result.append(q)
                print(q)
                if q=='G':
                    print("Search Completed. Goal achieved.")
                    break
                
                for i in reversed(self.graph[q]):
                    if i not in visited:
                        s1.push(i)
                    
        
#Task 1: Graph implementation

g=graph()
g.addnode(1)
g.addnode(2)
g.addnode(3)
g.addnode(4)
g.addnode(5)
g.addnode(6)
g.addnode(7)
g.addnode(8)
g.addnode(9)
g.addnode(10)
g.addnode(11)
g.addnode(12)

g.addedge(2,1)
g.addedge(7,1)
g.addedge(8,1)
g.addedge(2,3)
g.addedge(2,6)
g.addedge(3,4)
g.addedge(3,5)
g.addedge(8,9)
g.addedge(12,8)
g.addedge(9,10)
g.addedge(9,11)
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

print("DFS Implementation")
g1.DFS('A')