def kadanesAlgorithm(array):
    # Write your code here.
    if not array:
        return None
    maxSum = float('-inf')
    currSum = 0
    for value in array:
        currSum = max(value, currSum + value)
        maxSum = max(maxSum, currSum)

    return maxSum
if __name__=="__main__":
    array_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(kadanesAlgorithm(array_1))