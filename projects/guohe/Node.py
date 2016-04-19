class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None
        """ Initiate link list structure """

    def remove(self, data, previousNode):
        if self.data == data:
            previousNode.nextNode = self.nextNode
            del self.data
            del self.self.nextNode
        elif self.nextNode is not None:
            self.nextNode.remove(data, self)
        """ Use recursive to find the right node """
