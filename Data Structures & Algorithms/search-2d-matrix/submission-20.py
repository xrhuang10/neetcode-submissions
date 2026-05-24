class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            middlerow = top + (bottom - top)//2

            if matrix[middlerow][0] <= target and target <= matrix[middlerow][-1]:
                l, r = 0, len(matrix[middlerow]) - 1
                while l <= r:
                    m = l + (r-l)//2
                    if matrix[middlerow][m] == target:
                        return True
                    elif target > matrix[middlerow][m]:
                        l = m + 1
                    else:
                        r = m - 1
                return False
            
            elif matrix[middlerow][0] > target:
                bottom = middlerow - 1
            
            elif matrix[middlerow][-1] < target:
                top = middlerow + 1


        return False
