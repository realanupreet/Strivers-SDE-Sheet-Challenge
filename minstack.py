class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            if self.minstack[-1] >= val:
                self.minstack.append(val)
        else:
            self.minstack.append(val)

        # print(self.stack)
        print(self.minstack)

    def pop(self) -> None:
        if self.stack[-1] == self.minstack[-1]:
            self.stack.pop()
            self.minstack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        print(self.stack[-1])
        return(self.stack[-1])

    def getMin(self) -> int:
        print(self.minstack[-1])
        return (self.minstack[-1])

        # print("Hellow")
minStack = MinStack()  # ;
# ["MinStack","push","push","push","getMin","pop","getMin"]
minStack.push(0)  # ;
minStack.push(1)  # ;
minStack.push(0)  # ;
minStack.getMin()  # ; // return -2
minStack.pop()  # ;
minStack.getMin()  # ; // return -2
# minStack.push(0)  # ;
# minStack.push(-3)  # ;
# minStack.getMin()  # ; // return -3
# minStack.top()  # ;    // return 0
