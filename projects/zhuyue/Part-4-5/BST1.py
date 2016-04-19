class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.value=val
        
class BST:
    def __init__(self):
        self.root=None
    
    ###########################################    
    def insert(self,val):
        self.root=self._insert(self.root,val)
        
    def _insert(self,ptr,val):
        if ptr is None:
            return Node(val)
        elif ptr.value==val:
            return ptr
        elif ptr.value < val:
            ptr.right=self._insert(ptr.right,val)
        else:
            ptr.left=self._insert(ptr.left,val)
        return ptr
   ############################################     
    def search(self,val):
        self._search(self.root,val)
        
    def _search(self,ptr,val):
        if ptr is None:
            return False
        elif ptr.value == val:
            return True
        elif ptr.value < val:
            self._search(ptr.right,val)
        else:
            self._search(ptr.left,val)
    ############################################    
        
    def delete(self,val):
        self._delete(self.root,val)
        
    def _delete(self,ptr,val):
        if ptr is None:
            return None
        elif ptr.value < val:
            ptr.right=self._delete(ptr.right,val)
        elif ptr.value > val:
            ptr.left=self._delete(ptr.left,val)
        else:
            if ptr.left is None or ptr.right is None:
                ptr=ptr.left if ptr.right is None else ptr.right
            else:
                temp=ptr.right
                while(temp1.left is not None):
                    temp=temp.left
                ptr.value=temp.value
                ptr.right=self._delete(ptr.right,temp.value)
        return ptr
    ############################################    
    def inorder(self):
        self._inorder(self.root)
        
    def _inorder(self,ptr):
        if ptr is not None:
            self._inorder(ptr.left)
            print(" "+str(ptr.value))
            self._inorder(ptr.right)
            
    ############################################        
    def min(self):
        return self._min(self.root)
        
    def _min(self,ptr):
        if ptr is None:
            return None
        elif ptr.left is None:
            return ptr.value
        else:
          return self._min(ptr.left)  
    ############################################
    def lowestCommanAncestor(self,val1,val2):
        temp=val1 if val1>val2 else val2
        val2=val1+val2-temp
        return self._lowestCommanAncestor(self.root,temp,val2)
        
    def _lowestCommanAncestor(self,ptr,val1,val2):
        if ptr.value>=val2 and ptr.value<=val1:
            return ptr.value
        elif ptr.value > val1:
            return self._lowestCommanAncestor(ptr.left,val1,val2)
        else:
            return self._lowestCommanAncestor(ptr.right,val1,val2)
    
    ############################################
    
    
def main():
    b=BST()
    b.insert(20)
    b.insert(10)
    b.insert(30)
    b.delete(10)
    b.insert(5)
    b.insert(6)
    b.insert(35)
    b.delete(30)
    b.insert(15)
    b.insert(3)
    b.insert(4)
    b.insert(2)
    b.inorder()
    print b.lowestCommanAncestor(20,35)
    print b.lowestCommanAncestor(5,6)
    print b.lowestCommanAncestor(2,4)
main()