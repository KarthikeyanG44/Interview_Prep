"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

The algorithm proposed here does a binary search on all the rows
Time Complexity : O(MlogN)
Space Complexity : O(1)
"""

class Solution:
    def binarySearch(self, array, num, beg, end):
        if end >= beg:
            mid = int((beg + end) / 2)
            if array[mid] == num:
                return True
            elif array[mid] < num:
                return self.binarySearch(array, num, mid + 1, end)
            else:
                return self.binarySearch(array, num, beg, mid - 1)
        else:
            return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        nRows = len(matrix)
        nCols = len(matrix[0])

        isFound = False

        for row in range(nRows):
            if isFound:
                return isFound
            isFound = self.binarySearch(matrix[row], target, 0, nCols - 1)

        return isFound

if __name__=="__main__":
    s = Solution()
    two_D_array = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    target_to_find = 23
    print(s.searchMatrix(two_D_array,target_to_find))