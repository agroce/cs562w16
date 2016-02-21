### Linked lists (ch2, cracking the coding interview)

#https://github.com/ImrulKayes/DataStructuresAlgorithms/blob/master/linkedList-1.py

###creating a linked list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class linkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        if self.head==None:
            newNode=ListNode(data)
            self.head=newNode
        else:
            head=self.head
            while head.next:
                head=head.next
            newNode=ListNode(data)
            head.next=newNode   

    def getHead(self):
        return self.head
    def getTail(self):
        head=self.head
        while head.next:
            head=head.next
        return head
    
    def printList(self,head=None):
        print "{{{{{{{{{{{{{{{{{{{{{{{{{{{"
        if head==None:
           head=self.head
        while head!=None:
            print head.val
            head=head.next
        print "}}}}}}}}}}}}}}}}}}}}}}}}}}}}"

    def ReversePrint(self,head):
        print ">->->->->->->->->->->->->->->"
        if not head:
            return
        if  head.next is None:
            print head.val
            return
        
        prev=None
        curr=head
        while curr:
            oldPrev=prev
            prev=curr
            curr=curr.next
            prev.next=oldPrev
        while prev:
            print prev.val
            prev=prev.next
        print "<-<-<-<-<-<-<-<-<-<-<-<-<-<-<"

    def deleteNode(self, node):
        "Write a function to delete a node (except the tail) in a singly linked list, given only access to that node."
        "just copy next node value to this node and delete next node"
        if not node:    return
        node.val=node.next.val
        node.next=node.next.next

    def reverseList(self, head):
        if not head or not head.next:   return
        
        prev=None
        curr=head
        while curr:
            oldPrev=prev
            prev=curr
            curr=curr.next
            prev.next=oldPrev
        return prev
    
    def removeElements(self, head, val):
        # remove nodes from the list which have val
        current=head
        if head==None:
            return
        
        dummy=ListNode(0) # used as a header
        currD=dummy  # use to traverse the list
        
        while current:
            # if we keep this node, set this as dummy's current's next node, set dummy's current to this node
            if current.val!=val:
                currD.next=current
                currD=current
            # else not need to do anything with dummy's current node
            current=current.next
        # finally, remember to set dummy's current's next node to None, although we delete middle elemnets we don't have to do it, but considering deleting last element
        currD.next=None
        return dummy.next
                
            
    def deleteDuplicates(self, head):
        # Given a sorted linked list, delete all duplicates such that each element appear only once.
        # an iterative solution is below
        if head==None or head.next==None:
            return head
        else:
            # if this node is similar to next node, return the head we get from the list which has next node as a head
            if head.val==head.next.val:
                head=self.deleteDuplicates(head.next)
                return head
            else:
                # otherwise get head from the list which has next node as a head and connect this node with that head
                nextNode=self.deleteDuplicates(head.next)
                head.next=nextNode
                return head

    def getIntersectionNode(self, headA, headB):
       # Write a program to find the node at which the intersection of two singly linked lists begins.
       # get the lenghth difference first and advance the current pointer of larger length upto that difference
       # then advance both current pointers until they are the same
        curA,curB = headA,headB
        lenA,lenB = 0,0
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next
        curA,curB = headA,headB

        # reduce the length difference by advancing the larger node's current 
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next
        # now when two points's will meet at intersection
        # even when no intersection, they will meet at None
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA


    def mergeTwoLists(self, l1, l2):
        # marge two sorted lists into a list
        currentA=l1
        currentB=l2
        head=None
        
        if currentA==None and currentB==None: 
            return None
        if currentA==None or currentB==None: 
            if currentA==None: 
                return currentB
            else:
                return currentA
        
        dummy=head
        head=ListNode(0)
        dummy=head
        # set dummy's next node as the lowest node
        while currentA and currentB:
            if currentA.val<=currentB.val:
                head.next=currentA
                head=currentA
                currentA=currentA.next
            else:
                head.next=currentB
                head=currentB
                currentB=currentB.next

        # if both lists are exhausted
        if currentA==None and currentB==None: 
            head.next=None
            return dummy.next
        # if any of the list exists
        else:
            if currentA:
                while currentA:
                    head.next=currentA
                    head=currentA
                    currentA=currentA.next
            else:
                while currentB:
                    head.next=currentB
                    head=currentB
                    currentB=currentB.next
        head.next=None
        return dummy.next

    def swapPairs1(self, head):
        # we are taking 2 pairs at a time and adjusting the next pointers, flag is for setting the head, e.g., 1,2,3,4 see below
        # a much much simpler solution using recursion is below
        if head==None:
            return
        current=head
        flag=True
        while current and current.next:
            nextPairHead=current.next.next
            next=current.next
            next.next=current
            if flag:
                head=next
                flag=False
            # e.g., 1,2,3,4, first iteration we have got 2,1 but what will be the next of 1, it will be None if nextPairHead doesn't exist,
            # else will be nextPairHead.next (e.g.,4) or will be nextPairHead (if the list was 1,2,3)
            if nextPairHead:
                if nextPairHead.next:
                    current.next=nextPairHead.next
                else:
                    current.next=nextPairHead
            else:
                current.next=None
            current=nextPairHead                    
            return head
        
    def swapPairs(self, head):
        # Given a linked list, swap every two adjacent nodes and return its head.
        # use recursion, e.g., 1,2,3,4 3,4 will give a head and process that after swapping 1,2 and return head
        if not head or not head.next:
            return head
        newhd=head.next
        head.next=self.swapPairs(newhd.next)
        newhd.next=head
        return newhd
                    

    def hasCycle(self, head):
        # keep two pointers, one advances by one and other by two. if they meet there is a cycle
        if not head or not head.next:
            return False
        first=head
        second=head.next
        while first and second:
            if first==second:
                return True
            first=first.next
            # we need to check whether second.next.next is possible
            if second.next:
                second=second.next.next
            else:
                second=second.next
        return False

    
    def detectCycle(self, head):
        # this is called Floyd's cycle-finding algorithm, also know as tortoise and hare algorithm
        #http://yucoding.blogspot.com/2013/12/leetcode-question-linked-list-cycle-ii.html
        if head==None:
            return None
        first = head
        second=head
        while second.next and second.next.next:
            first = first.next
            second = second.next.next
            if first == second:
                second=head
                while second!=first:
                    second=second.next
                    first=first.next
                return first
        return None

    def reorderList(self, head):
        # Reorder to L(0)->l(n)->L(1)->L(n-1)...
        # dont do anything if list has less than three nodes
        if head==None or head.next==None:
            return
        if head.next.next==None:
            return

        # take all the nodes in a queue
        length=1
        current=head
        while current.next!=None:
            current=current.next
            length+=1
        q=[]
        current=head

        for i in range(length):
            q.append(current)
            current=current.next

        # pop one node at a time, add it to current node, update current node, only length/2 iteration is enough    
        current=head
        for i in range(int(length/2)):
            nextNode=current.next
            newNode=q.pop()
            current.next=newNode
            newNode.next=nextNode
            current=nextNode
        # current node next should be none after reordering
        current.next=None

    def rotateRight(self, head, k):
        # Given a list, rotate the list to the right by k places, where k is non-negative.
        # very intuitive get to the n-k-1th element and reorder head
        
        if k==0 or not head or not head.next:
            return head
        current=head
        length=0

        # get the length
        while current:
            current=current.next
            length+=1
        # for rotating larger than the length w
        k=k%length
        if k==0 or k==length:
            return head
        else:
            # reorder
            current=head
            for i in range(length-k-1):
                current=current.next
            newHead=current.next
            current.next=None
            newCurrent=newHead

            while newCurrent.next:
                newCurrent=newCurrent.next
            newCurrent.next=head
            return newHead

    def addTwoNumbers(self, l1, l2):
        # You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
        head=curr=ListNode(0)
        c=0
        while l1 or l2:
            sum=0
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            prev=curr
            curr=ListNode((c+sum)%10)
            prev.next=curr 
            c=(c+sum)/10
        if c==1:
            curr.next=ListNode(1)
        return head.next 

#l=linkedList()
#l.insert(1)
#l.insert(2)
#l.insert(1)
#l.insert(4)
#l.insert(5)

#l1=linkedList()
#l1.insert(5)
#l1.insert(6)
#l1.insert(4)
#l1.insert(9)
#l1.insert(7)


#head=l.getHead()
#l.ReversePrint(head)
#l.printList(head1)
#l.removeElements(head,"2")
#head=l.getHead()
#print head.val
#x=l.deleteDuplicates(head)
#print x.val
#l.printList(x)

#headA=l.getHead()
#headB=l1.getHead()
#l.printList(headA)
#print "ass"
#l1.printList(headB)
#x=l.getIntersectionNode(headA,headB)
#x=l.removeNthFromEnd(head,1)
#x=l.mergeTwoLists(headB,headA)
#x=l.deleteDuplicates(headA)
#print x.val
#l.printList(x)
#tail=l.getTail()
#tail.next=headA
#print l.hasCycle(headA)
#print l.detectCycle(headA).val
#l.reorderList(headA)
#x=l.rotateRight(headA,3)
#l.printList(x)
#x=l.addTwoNumbers(headA,headB)
#l.printList(x)