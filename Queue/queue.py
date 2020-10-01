class Queue:
    def __init__(self):
        self.queue = []

    # Add element
    def enqueue(self, item):
        self.queue.append(item)

    # remove element
    def dequeue(self):
        # check size of queue
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display queue
    def display(self):
        print(self.queue)

    # show size
    def size(self):
        print(len(self.queue))


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

q.display()
