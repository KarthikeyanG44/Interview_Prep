class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return A
        if len(A) == 1:
            return A[0]

        n = len(A)

        max_sum = - float('inf')
        sub_array_indices = [0, 0]
        for i in range(n):
            j = i + 1
            if (j > n - 1):
                j = 0
            while (j != i):
                print(i, j, max_sum)
                if (i < j):
                    local_subarray_sum = sum(A[i:j])
                else:
                    local_subarray_sum = sum(A[i:]) + sum(A[:j])

                temp_max_sum = max(max_sum, local_subarray_sum)

                if (temp_max_sum != max_sum):
                    sub_array_indices[0], sub_array_indices[1] = i, j
                    max_sum = max(max_sum, temp_max_sum)

                j += 1
                if (j > n - 1):
                    j = 0

        return max_sum