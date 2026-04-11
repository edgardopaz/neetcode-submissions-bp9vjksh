class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                # search this matrix
                low = 0
                high = len(matrix[i])
                while low <= high:
                    mid = (low + high) // 2
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] < target:
                        low = mid + 1                        
                    else:
                        high = mid - 1
            else:
                continue

        return False