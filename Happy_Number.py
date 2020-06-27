"""
A happy number is defined as follows:
1 . Start with a number
2. Replace the number by the sum of squares of it's digits
3. Continue doing this till the number converges to 1
"""
"""
One unique property of a Happy Number is that during the iteration of summing the squares of it's digits , it never encounters a result previously encountered. 
In other words, it does not form a loop. We can either keep a track of results so far and check if we have gotten a result we already got. 
Or we can use the slow and fast pointer approach that is used to detect cycle in a linked list. The same is implemented in this code
"""

class HappyNumber:
    def getDigitsSum(self, n):
        digitsSquareSum = 0
        while (n):
            digitsSquareSum += (n % 10) * (n % 10)
            n = int(n / 10)

        return digitsSquareSum

    def isHappy(self, n):
        slowPtr = n
        fastPtr = n
        while (True):

            # move slow number
            # by one iteration
            slowPtr = self.getDigitsSum(slowPtr)

            # move fast number
            # by two iteration
            fastPtr = self.getDigitsSum(self.getDigitsSum(fastPtr))
            if (slowPtr != fastPtr):
                continue
            else:
                break

                # if both number meet at 1,
        # then return true
        return (slowPtr == 1)

if __name__=="__main__":
    num1 = 19
    num2 = 20
    happyNumberChecker = HappyNumber()
    if (happyNumberChecker.isHappy(num1)):
        print(num1,"is a Happy Number")
    if (happyNumberChecker.isHappy(num2)):
        print(num2,"is a Happy Number")
    else:
        print(num2, "is NOT a Happy Number")