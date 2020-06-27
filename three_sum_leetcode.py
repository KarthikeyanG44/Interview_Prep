def threeSum(nums) :
    if not nums or len(nums) < 3:
        return []

    threeSumSubsets = []

    nums.sort()
    n = len(nums)

    for idx in range(n - 2):
        if idx > 0 and nums[idx] == nums[idx - 1]:
            continue
        ptr1 = idx + 1
        ptr2 = n - 1
        while (ptr2 > ptr1):
            current_sum = nums[idx] + nums[ptr1] + nums[ptr2]
            if current_sum == 0:
                current_list = [nums[idx], nums[ptr1], nums[ptr2]]
                threeSumSubsets.append(current_list)
                while ptr1 < ptr2 and nums[ptr1] == nums[ptr1+1]:
                    ptr1 += 1
                while ptr1 < ptr2 and nums[ptr2] == nums[ptr2 - 1]:
                    ptr2 -= 1
                ptr1 += 1
                ptr2 -= 1
            elif current_sum < 0:
                ptr1 += 1
            else:
                ptr2 -= 1

    return threeSumSubsets


if __name__=="__main__":
    array = [-2,0,0,2,2]
    answer = threeSum(array)
    print(answer)
