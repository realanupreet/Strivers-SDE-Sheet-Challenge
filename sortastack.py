stack = [5, -2, 9, -7, 3]

# temp = []
# res = []


def insert(stack, ele):
    if len(stack) == 0 or stack[-1] < ele:
        stack.append(ele)
        return
    a = stack.pop()
    insert(stack, ele)
    stack.append(a)
    pass


def solve(stack):
    if len(stack) == 1:
        return
    a = stack.pop()
    solve(stack)
    insert(stack, a)
    # res.extend(temp)
    pass


solve(stack)
