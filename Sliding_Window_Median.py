def medianSlidingWindow(nums, k):
    if not nums or len(nums) == 1:
        return nums

    median_list = []

    start = 0
    end = k

    while end <= len(nums):
        local_list = nums[start:end]
        local_list.sort()
        if (k % 2 != 0):
            localMedianIndex = int(k/2)
            median_list.append(local_list[localMedianIndex])
        else:
            localMedianIndex1, localMedianIndex2 =  k/ 2, k/2 + 1
            localMedian = (local_list[localMedianIndex1] + local_list[localMedianIndex2]) / 2
            median_list.append(localMedian)

        start += 1
        end += 1

    return median_list

if __name__ == "__main__":
    arr = [1,3,-1,-3,5,3,6,7]
    k = 3
    sliding_median = medianSlidingWindow(arr,k)
    print(sliding_median)