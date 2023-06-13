# the naive not to do in a interview solution
# does the job but at the cost of optimality

class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        # print("appended",num)

    def findMedian(self) -> float:
        self.arr.sort()
        # print(self.arr)
        # print(len(self.arr)//2)
        k = self.arr[len(self.arr)//2] if len(self.arr) % 2 != 0 else (
            self.arr[len(self.arr)//2]+self.arr[len(self.arr)//2 - 1])/2
        # print(k)
        return(k)


medianFinder = MedianFinder()  # ;
medianFinder.addNum(1)  # ;    // arr = [1]
medianFinder.addNum(2)  # ;    // arr = [1, 2]
medianFinder.addNum(4)  # ;    // arr = [1, 2]
medianFinder.addNum(8)  # ;    // arr = [1, 2]
medianFinder.findMedian()  # ; // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)  # ;    // arr[1, 2, 3]
medianFinder.findMedian()  # ; // return 2.0
