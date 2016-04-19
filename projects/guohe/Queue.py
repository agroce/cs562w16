class Queue(object):

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue ==[]

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)
