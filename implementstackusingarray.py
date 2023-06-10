# lifo last in first out
# push
# pop
# peek

class Stack:
    def __init__(self):
        self.top = -1
        self.stack = []*100

    def push(self, val):
        self.top += 1
        self.stack[self.top] = val

    def pop(self):
        self.top -= 1
        return self.stack[self.top+1]

    def peek(self):
        return self.stack[self.top]

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def size(self):
        return self.top+1
