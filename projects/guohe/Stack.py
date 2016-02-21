class Stack(object):

    def __init__(self):
        self.stack = []
        self.numOfItems = 0

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.insert(self.numOfItems, data)
        self.numOfItems = self.numOfItems + 1

    def pop(self):
        self.numofitems = self.numofitems - 1
        datatoReturn = self.stack.pop(self.numOfItems)
        return datatoReturn

    def size(self):
        return len(self.stack)
    def search(self,data):
        for(i=0,i<numOfItems)