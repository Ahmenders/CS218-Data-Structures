class Node:
    def __init__(self, val=None):
        self.val=val
        self.next=None 

class Ring:
    def __init__(self):
        self.head=None

def _get_last(self):
    temp = self.head
    
    if temp is None:
        return None
    temp=temp.next
    while temp.next!=self.head:
        temp=temp.next
        
    return temp

Ring._get_last=_get_last

def insert(self,index,val):
    
    new_node=Node(val)
    last = self._get_last()
    
    if index==0:
        new_node.next=self.head
        self.head=new_node
        #new_node.next=self.head
        #return
    
        if last is None:
            self.head.next=self.head
        else:
            last.next=new_node

        return
            
    
    if self.head is None:
        raise IndexError("list is out of range")
        
    
    counter=0
    
    temp=self.head
    while temp is not None and counter<index:
        prev=temp
        temp=temp.next
        counter+=1
        
    prev.next=new_node
    new_node.next=temp
    
Ring.insert=insert

def __str__(self):
    r='['
    temp=self.head
    while temp is not None:
        r+=str(temp.val)+", "
        temp=temp.next
        
        if temp==self.head:
            break
    r=r.rstrip(", ")
    r+="]"
    return r
Ring.__str__=__str__

def len(self):
    if self.head is None:
        return 0
    counter=1
    temp=self.head
    while temp.next!=self.head:
        temp=temp.next
        counter +=1
        
    return counter
Ring.len=len

def push(self,val):
    if self.head is None:
        self.insert(0,val)
    else:
        self.insert(self.len(),val)
Ring.push=push

def remove(self,val):
    if self.head is None:
        raise Exception("cant remove from empty list")
    
    temp=self.head
    last=self._get_last()
    
    if self.head.val==val:
        if last==self.head:
            self.head=None
        else:
            self.head=temp.next
            last.next=self.head
        return
    
    prev=temp
    temp=temp.next
    while temp!=self.head:
        if temp.val==val:
            break
        prev=temp
        temp=temp.next
    
    if temp==self.head:
        #raise Exception("Value not found")
        return
    prev.next=temp.next
Ring.remove=remove

def pop(self):
    if self.head is None:
        raise IndexError("list is out of range")
    
    last=self._get_last().val
    self.remove(last)
    return last
Ring.pop=pop

###ANOTHER LOGIC FOR POP

#def pop(self):
 #   if self.head is None:
  #      return 
   # temp=self.head
    #if temp.next==self.head:
#        self.head =None
#        return
#    prev=temp
#    temp=temp.next
#    while temp.next!=self.head:
#        prev=temp
#        temp=temp.next
#    prev.next=self.head
#Ring.pop=pop

def get(self,index):
    if self.head is None:
        raise IndexError("list is empty")
        
    temp=self.head
    counter=0
    while counter<index:
        temp=temp.next
        counter+=1
    return temp.val
Ring.get=get


def remove_at(self,index):
    if self.head is None:
        return None
    temp=self.head
    last=self._get_last()
    
    if index==0:
        if last==self.head:
            self.head=None
        else:
            self.head=temp.next
            last.next=self.head
        return
    
    prev=temp
    temp=temp.next
    counter=1
    while counter<index:
        prev=temp
        temp=temp.next
        counter+=1
    prev.next=temp.next
Ring.remove_at=remove_at

####ANOTHER LOGIC OF remove_at ######

#def remove_at(self,index):
 #   if self.head is None:
  #      return None
   # val=self.get(index)
   # self.remove(val)
#Ring.remove_at=remove_at    

if __name__ == '__main__': 
    r = Ring()
    # r.insert(1, 1)
    r.insert(0, 1)
    r.insert(0, 2)
    r.insert(1, 3)
    r.insert(7, 5)  # different behavrior since it's a ring! 
    print(r)
