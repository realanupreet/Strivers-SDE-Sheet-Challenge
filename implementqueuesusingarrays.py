# fifo
# push
# pop
# peek

class Queue:
    def __init__(self):
        self.front = 1
        self.rear = 1
        self.queue = [-1]*100
        self.size = 0

    def push(self, val):
        if self.size < 100:
            self.queue[self.rear] = val
            self.rear += 1
            self.size += 1
            # print(self.queue, self.rear, self.size)
        else:
            print("yup, didnt actually have enough space")

    def pop(self):
        self.front += 1
        self.size -= 1
        return self.queue[self.front-1]

    def peek(self):
        return self.queue[self.front]

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def qsize(self):
        if self.front != self.rear:
            return self.size
        else:
            return "no worries"


myq = Queue()

myq.push(5)
myq.push(6)
print(myq.qsize())
