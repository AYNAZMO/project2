class queue:
    def __init__(self):
        self.MAX_QUEUE_SIZE = 100
        self.rear = -1
        self.front = -1
        self.arr = [0] * self.MAX_QUEUE_SIZE

    def reverse_queue(self):
        if self.IsEmpty():
            print("Queue is empty")
            return
        reverse = queue()
        temp = []
        for i in range(self.front, self.rear + 1):
            temp.append(self.arr[i])

        for a in reversed(temp):
            reverse.enqueue(a)

        return reverse
        
    def enqueue(self, value):
        if self.IsFull():
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.arr[self.rear] = value

    def dequeue(self):
        if self.IsEmpty():
            print("Queue is empty")
            return
        self.front += 1
        if self.front > self.rear:
            self.front = self.rear = -1

    def IsFull(self):
        return self.rear == self.MAX_QUEUE_SIZE - 1

    def IsEmpty(self):
        return self.front == -1 or self.front > self.rear

    def display(self):
        if self.IsEmpty():
            print("Queue is empty")
            return
        print("Values: ")
        for i in range(self.front, self.rear + 1):
            print(self.arr[i])

    def peek(self):
        if self.IsEmpty():
            print("Queue is empty")
            return
        return self.arr[self.front]
    




q1 = queue()
q1.enqueue(12)
q1.enqueue(3)
q1.enqueue(62)
q1.enqueue(9)
q1.display()
print("///////////////////////////")
q1.dequeue()
q1.display()
print("///////////////////////////")

print("front item: ",q1.peek())

print("///////////////////////////")

q2 = queue()
q2 = q1.reverse_queue()
q2.display()
