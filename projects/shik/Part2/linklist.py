class Node(object):
    """ Node """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
        

class LinkList(object):
    """ LinkList """
    def __init__(self, datas=None):
        self.head = Node(0)
        if datas:
            self.create_by_tail(datas)

    def __repr__(self):
        """
        rewrite print string, format like:
        x->x->x->...->]
        """
        p = self.head
        reprstr = str(p.data) + '->'
        while p.next:
            reprstr += str(p.next.data)
            reprstr += '->'
            p = p.next
        reprstr += ']'
        return reprstr

    def __len__(self):
        """
        count the length of the LinkList by go through the list
        """
        length = 1
        p = self.head
        while p.next:
            length += 1
            p = p.next
        #print length
        return length


   

    def create_by_head(self, datas):
        """
        create a LinkList by using data in datas(a list)
        every data will be added at the head of the list
        """
        self.clear()
        self.head = Node(datas[0])
        for i in datas[1:]:
            cur_node = Node(i)
            cur_node.next = self.head
            self.head = cur_node

    def create_by_tail(self, datas):
        """
        create a LinkList by using data in datas(a list)
        every data will be added at the tail of the list
        """
        self.clear()
        self.head = Node(datas[0])
        p = self.head
        for i in datas[1:]:
            cur_node = Node(i)
            p.next = cur_node
            p = p.next

    def clear(self):
        """ clear the list """
        self.head = Node(0)

    def is_empty(self):
        """ whether the list is empty """
        if len(self) == 0:
            print "True"
            return True
        else:
            print "False"
            return False

    def getData_by_index(self, index):
        """
        :param index: position of the node in the list.
        :return: the data on the index of False if not exist.
        """
        count = 0
        p = self.head
        while p.next:
            if count == index:
                return p.data
            else:
                p = p.next
                count += 1
        return False

    def getData_by_value(self, value):
        """
        :param index: value of the node in the list.
        :return: position of the first data that fit the value 
            or False if not exist.
        """
        count = 0
        p = self.head
        while p.next:
            if p.data == value:
                return count
            else:
                p = p.next
                count += 1
        return False

    def insertData(self, index, data):
        """
        :param index: the position to insert data to.
        :param data: the data to insert into list.
        :return: True or False.
        """
        count = 1
        p = self.head
        while p.next:
            if count == index:
                new_node = Node(data)
                new_node.next = p.next
                p.next = new_node
                p = p.next
                return True
            else:
                p = p.next
                count += 1
        return False

    def deleteData_by_index(self, index):
        """
        :param index: position of the node to delete.
        :return: True or False.
        """
        count = 1
        p = self.head
        while p.next:
            if count == index:
                p.next = p.next.next
                p = p.next
                print self
                return True
            else:
                p = p.next
                count += 1
        return False

    def deleteData_by_value(self, value):
        """
        :param index: value of the node to delete.
        :return: True or False.
        """
        count = 0
        p = self.head
        while p.next:
            if p.next.data == value:
                p.next = p.next.next
                p = p.next
                # print self
                return True
            else:
                p = p.next
                count += 1
        return False

    def delete_repeat(self):
        """
        delete repeat node in list
        """
        p = self.head #p for go through list from head one by one
        while p:
            q = p #q for modify list
            r = p.next #r for go through and compare with p 
            while r:
                if r.data == p.data:
                    q.next = r.next
                    r = q.next
                    # print 'delete:' + p.data
                else:
                    q = r
                    r = r.next
            p = p.next

    def delete_one(self, value):
        """
        delete all node of the value in list
        """
        # while self.getData_by_value(value):
        #     self.deleteData_by_value(value)
        p = self.head
        q = p.next
        while q:
            if q.data == value:
                p.next = q.next
                q = p.next
            else:
                p = q
                q = q.next

def merge_linklist(list_a, list_b):
    """
    merge two ordered list to a new list
    """
    a = list_a.head
    b = list_b.head
    list_c = LinkList()
    if a.data > b.data:
        list_c.head = b
        b = b.next
    else:
        list_c.head = a
        a = a.next
    c = list_c.head
    while a and b:
        if a.data > b.data:
            c.next = b
            c = b
            b = b.next
        elif a.data < b.data:
            c.next = a
            c = a
            a = a.next
        elif a.data == b.data:
            c.next = a
            c = a
            a = a.next
            b = b.next
            # list_b.deleteData_by_value(b.data)
    if a:
        c.next = a
    else:
        c.next = b
    return list_c

    def reverse(self):
        pass


#############################
#############################
#############################


class CirList(LinkList):
    """CirList"""

    def create_by_head(self, datas):
        """
        create a LinkList by using data in datas(a list)
        every data will be added at the head of the list
        """
        self.clear()
        self.head = Node(datas[0])
        for i in datas[1:]:
            cur_node = Node(i)
            cur_node.next = self.head
            self.head = cur_node
        p = self.head
        while p.next:
            p = p.next
        p.next = self.head

    def create_by_tail(self, datas):
        """
        create a LinkList by using data in datas(a list)
        every data will be added at the tail of the list
        """
        self.clear()
        self.head = Node(datas[0])
        p = self.head
        for i in datas[1:]:
            cur_node = Node(i)
            p.next = cur_node
            p = p.next
        p.next = self.head

    def is_empty(self):
        """ whether the list is empty """
        if self.head.next == self.head:
            print "True"  
        else:
            print "False"
            

    def printList(self,head=None):
        if head==None:
           head=self.head
        while head!=None:
            print head.val
            head=head.next     



if __name__ == '__main__':
    intdatas_1 = [1,'a',2,'b']
    intdatas_2 = range(0, 20, 4)

    chardatas = ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'c', 'g', 'd']
    print 'Prepare 2 int list:\n' + str(intdatas_1) + \
         '\n' + str(intdatas_2) + \
        '\nand char list:\n' + str(chardatas) + '\nfor create 3 lists...'

    llst_i_1 = LinkList()
    llst_i_2 = LinkList()
    llst_c = LinkList(chardatas)
    print 'Create char linklist by head: ' + str(llst_c)
    llst_i_1.create_by_head(intdatas_1)
    
    llst_i_2.create_by_tail(intdatas_2)
    llst_i_1.is_empty()
    print 'Create int linklist 1 by head: ' + str(llst_i_1)
    print 'Create int linklist 2 by tail: ' + str(llst_i_2)
    
    print 'merge 2 int list(ordered) to one:'
    #print merge_linklist(llst_i_1, llst_i_2)
    llst_i_1.insertData(2,9)
   # print 'New linklist 1 by insertData: ' + str(llst_i_1)



    #llst_c.delete_repeat()
    print llst_c