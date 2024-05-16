class Queue:
    def __init__(self): #Init items 
        self.items = []

    def is_empty(self): #Is the queue empty?
        return len(self.items) == 0

    def enqueue(self, item):#Add an item to the queue
        self.items.append(item)

    def dequeue(self): #Remove an item from the queue
        if self.is_empty():#Checking if the queue is empty
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():#We can't peek if empty
            raise IndexError("Cannot peek at an empty queue")
        return self.items[0]

    def size(self):#How many are there??
        return len(self.items)
    
    
myqueue = Queue()
myqueue.enqueue(2)
print(myqueue.peek())