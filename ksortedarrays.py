import heapq
a = [[1, 2, 3],
     [2, 4, 6],
     [0, 9, 10]
     ]
print(list(heapq.merge(*a)))
