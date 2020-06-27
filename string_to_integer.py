class Solution:
    def myAtoi(self, str):
        i = 0
        sgn, ans = 1, 0
        low, high = -2 ** 31, 2 ** 31 - 1
        while i < len(str):
            if str[i] == ' ':
                i += 1
                continue
            if str[i] in {'+', '-'}:
                if i + 1 >= len(str) or not str[i + 1].isdigit():
                    return 0
                sgn = 1 if str[i] == '+' else -1
                i += 1
            elif str[i].isdigit():
                while i < len(str) and str[i].isdigit():
                    ans *= 10
                    ans += int(str[i])
                    # overflow check
                    if sgn == 1 and ans > high:
                        return high
                    elif sgn == -1 and -ans < low:
                        return low
                    i += 1
                return int(sgn * ans)
            else:
                return 0

        return 0
if __name__ == "__main__":
    s = Solution()
    a = "+-2"
    print(s.myAtoi(a))