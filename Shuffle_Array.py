import random


class Solution(object):

    def __init__(self, nums):
        self.actual_list = list(nums)  ########## When assigning a list to another they share the same memory. SO it is better to create a new list() #####
        self.random_list = list(nums)


    def reset(self):
        return self.actual_list


    def shuffle(self):
        temp_array = list(self.random_list)
        n = len(self.random_list)
        for idx in range(n):
            rand_idx = random.randrange(len(temp_array))
            self.random_list[idx] = temp_array.pop(rand_idx)

        return self.random_list

if __name__ =="__main__":
    list1 = [1,2,3,4,5]
    s = Solution(list1)
    print(s.shuffle())
    print(s.reset())
    print(s.shuffle())