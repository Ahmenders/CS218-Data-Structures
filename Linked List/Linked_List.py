class Node:
    def __init__(self,val=None):
        self.val=val;
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

def push(self,val):
    new_node=Node(val)
    
    if self.head is None:
        self.head=new_node
        return
    
    temp=self.head
    
    while temp.next is not None:
        temp=temp.next
        
    temp.next=new_node
    
LinkedList.push=push

def pop(self):
    if self.head is None:
        raise Exception("List is Empty cannot pop")
        
    if self.head.next is None:
        val=self.head.val
        self.head=None
        return val
    
    temp=self.head
    while temp.next is not None:
        prev=temp
        temp=temp.next
        
    val=temp.val
    prev.next=None
    return val
LinkedList.pop=pop

def insert(self,index,val):
    new_node=Node(val)
    if index==0:
        new_node.next=self.head
        self.head=new_node
        return
    
    temp=self.head
    counter=0
    while temp is not None and counter<index:
        prev =temp
        temp=temp.next
        counter+=1
    prev.next=new_node
    new_node.next=temp
    
LinkedList.insert=insert

def remove(self ,val):
    
    temp=self.head
    
    if temp is not None:
        if temp.val==val:
            self.head=temp.next
            temp=None
            return
    while temp is not None:
        if temp.val==val:
            break
        prev=temp
        temp=temp.next
    
    if temp is None:
        return
    
    prev.next=temp.next
    
LinkedList.remove=remove


def get(self,index):

    counter=0
    temp=self.head
    
    while temp is not None:
        if counter==index:
            val=temp.val
            return val
        temp=temp.next
        counter+=1
        
    if temp is None or counter<index:
        raise IndexError("list index out of range")
        
LinkedList.get=get

def len(self):
    temp=self.head
    counter=0
    while temp is not None:
        temp=temp.next
        counter+=1
        
    return counter
    
LinkedList.len=len


def __str__(self):
    r="["
    temp =self.head
    while temp is not None:
        r+=str(temp.val)+", "
        temp=temp.next
    r=r.rstrip(", ")
    r+="]"
    return r
LinkedList.__str__=__str__

if __name__ == "__main__": 
    l = LinkedList() 
    l.push(5) 
    l.push(6) 

    print(l)

    print(l.len())

    l.pop() 
    print(l.len())

    print(l.get(0))
    l.get(2) # Should say "IndexError: Index out of bound"

