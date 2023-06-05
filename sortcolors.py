class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        c = 0
        for num in nums:
            if num == 0:
                a += 1
            elif num == 1:
                b += 1
            else:
                c += 1
        for i in range(a):
            print("i for 0 is", i)
            nums[i] = 0
        i = 0
        for i in range(a, b+a):
            print("i for 1 is", i)
            nums[i] = 1
        for i in range(a+b, a+b+c):
            print("i for 0 is", i)
            nums[i] = 2
