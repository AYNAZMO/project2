class cqueue:
    def __init__(self):
        self.MAX_QUEUE_SIZE = 100
        self.rear = -1
        self.front = -1
        self.arr = [0] * self.MAX_QUEUE_SIZE

    def reverse_queue(self):
        if self.IsEmpty():
            print("Queue is empty")
            return
        
        reverse = cqueue()
        temp = []
        f = self.front
        while True:
            temp.append(self.arr[f])
            if f == self.rear:
                break
            f = (f+1)% self.MAX_QUEUE_SIZE

        for i in reversed(temp):
            reverse.enqueue(i)

        return reverse       

    def enqueue(self, value):
        if self.IsFull():
            print("Queue is full")
            return
        if self.IsEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.MAX_QUEUE_SIZE
        self.arr[self.rear] = value

    def IsFull(self):
        return (self.rear + 1) % self.MAX_QUEUE_SIZE == self.front

    def IsEmpty(self):
        return self.front == -1        

    def dequeue(self):
        if self.IsEmpty():
            print("Queue is empty")
            return
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.MAX_QUEUE_SIZE

    def display(self):
        if self.IsEmpty():
            print("Queue is empty")
            return
        print("Values: ")
        i = self.front
        while True:
            print(self.arr[i])
            if i == self.rear:
                break
            i = (i+ 1)%self.MAX_QUEUE_SIZE

    def peek(self):
        if self.IsEmpty():
            print("Queue is empty")
            return
        return self.arr[self.front]        

cq1 = cqueue()
cq1.enqueue(12)
cq1.enqueue(3)
cq1.enqueue(62)
cq1.enqueue(9)
cq1.display()
print("///////////////////////////")
cq1.dequeue()
cq1.display()
print("///////////////////////////")
print("front item: ",cq1.peek())

print("///////////////////////////")
cq2 = cqueue()
cq2 = cq1.reverse_queue()
cq2.display()

