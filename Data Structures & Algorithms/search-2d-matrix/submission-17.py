class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        

        while top <= bottom:
            midrow = top + (bottom - top)//2
            if matrix[midrow][0] <= target and target <= matrix[midrow][-1]:
                print("hit")
                l = 0
                r = len(matrix[midrow]) - 1
                while l <= r:
                    m = l + (r-l)//2
                    if matrix[midrow][m] == target:
                        return True
                    elif matrix[midrow][m] > target:
                        r = m - 1
                    elif matrix[midrow][m] < target:
                        l = m + 1
                return False

            elif matrix[midrow][0] > target:
                bottom = midrow - 1
            elif matrix[midrow][-1] < target:
                top = midrow + 1
        return False