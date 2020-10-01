class CircularQueue:
    def __init__(self, sizeOfQueue):
        self.sizeOfQueue = sizeOfQueue
        # ex sizeOfQueue = 5 [None,None,None,None, None]
        self.queue = [None] * sizeOfQueue
        self.head = self.tail = -1

    # Inserting element into queue
    def enqueue(self, item):
        # if we append more item in the already defined queue size,
        # this will print out a message saying that the queue is full
        # and it would not append to the end of the queue
        if ((self.tail + 1) % self.sizeOfQueue == self.head):
            print('Circular queue is full \n')
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
        else:
            self.tail = (self.tail + 1) % self.sizeOfQueue
            self.queue[self.tail] = item

    def dequeue(self):
        if (self.head == -1):
            print('The Circular queue is empty \n')
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.sizeOfQueue
            return temp

    def printCQueue(self):
        if (self.head == -1):
            print('No elem in circular queue')
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=' ')
            print()
        else:
            for i in range(self.head, self.sizeOfQueue):
                print(self.queue[i], end=' ')
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=' ')
            print()


cQueue = CircularQueue(2)
cQueue.enqueue(1)
cQueue.enqueue(2)
cQueue.enqueue(3)
print('initial queue')
cQueue.printCQueue()

cQueue.dequeue()
print('removed element')
cQueue.printCQueue()
