nums = [1, 2, 2]
res = []
sub = []


def make(i):
    if i >= len(nums):
        ob = sub.copy()
        ob.sort()
        if ob not in res:

            res.append(ob)
        return
    sub.append(nums[i])
    make(i+1)
    sub.pop()
    make(i+1)
    pass


make(0)
