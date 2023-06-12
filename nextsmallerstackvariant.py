A = [39, 27, 11, 4, 24, 32, 32, 1]
stack = [A[0]]
ans = [-1]
for a in A[1:]:
    print("->", stack)
    # print("=>",ans)
    if a > stack[-1]:
        print("    ", a, ">", stack[-1])
        ans.append(stack[-1])
        stack.append(a)
    elif a == stack[-1]:
        print("eq", stack[-2])
        ans.append(stack[-2])
    else:
        while len(stack) > 0 and a <= stack[-1]:
            print("    ", a, "<", stack[-1])
            stack.pop()
            print("                   ", stack)
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(a)
# submitted
