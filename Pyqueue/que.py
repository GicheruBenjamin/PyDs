class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)
    
    
myqueue = Queue()
myqueue.enqueue(2)
print(myqueue.peek())