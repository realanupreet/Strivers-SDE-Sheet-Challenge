class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # def searchMatrix(matrix, target):

        m = len(matrix)
        n = len(matrix[0])
        if target == matrix[0][0] or target == matrix[m-1][n-1]:
            return True
        if target > matrix[m-1][n-1] or target < matrix[0][0]:
            return False
        trow = -1
        for i in range(m):
            # print("i is", i)
            if target == matrix[i][n-1] or target == matrix[i][0]:
                return True
            if target <= matrix[i][n-1] and target >= matrix[i][0]:
                # print(f"target lies in row", i)
                trow = i
                break

        beg = 0
        end = n-1

        while beg < end:
            mid = (beg+end)//2
            if target == matrix[trow][beg] or target == matrix[trow][end]:
                # print("while is true")
                return True
                break
            elif target == matrix[trow][mid]:
                # print("elif is true")
                return True
                break
            if target < matrix[trow][mid]:
                end = mid-1
            else:
                beg = mid+1
        return False
