heights = [2, 1, 5, 6, 2, 3]
stack = [{"index": 0, "height": heights[0]}]
maxa = -1
print(" ", stack)
for i, h in enumerate(heights[1:]):
    print(h, stack)
    index = i+1
    while stack and h < stack[-1]["height"]:
        maxa = max(maxa, stack[-1]["height"]*(i+1-stack[-1]["index"]))
        index = stack[-1]["index"]
        stack.pop()
        # calculate area
        pass
    # else:
    stack.append({
        "index": index,
        "height": h
    })
print("""
-------------popping-------------
""")


while stack:
    print(stack)
    maxa = max(maxa, (stack[-1]["height"])*(len(heights) - stack[-1]["index"]))
    stack.pop()

print(maxa)
