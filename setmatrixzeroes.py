class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row0 = []
        col0 = []
        for i in range(len(a)):
            # print(f"i[{i}] row contains {a[i]}")
            for j in range(len(a[i])):
                # print(f"j[{j}] containes {a[i][j]}")
                if a[i][j] == 0:
                    row0.append(i)
                    col0.append(j)

        for i in range(len(a)):
            for j in range(len(a[i])):
                if i in row0:
                    a[i][j] = 0
                if j in col0:
                    a[i][j] = 0
