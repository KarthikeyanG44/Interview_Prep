"""
Question : Given a integer value convert it into it's equivalent roman representation and return the same.
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        if not num:
            return None
        value_to_symbol_dict = dict()
        #### Define dictionaries ######
        value_to_symbol_dict[1] = 'I'
        value_to_symbol_dict[5] = 'V'
        value_to_symbol_dict[10] = 'X'
        value_to_symbol_dict[50] = 'L'
        value_to_symbol_dict[100] = 'C'
        value_to_symbol_dict[500] = 'D'
        value_to_symbol_dict[1000] = 'M'
        value_to_symbol_dict[4] = 'IV'
        value_to_symbol_dict[9] = 'IX'
        value_to_symbol_dict[40] = 'XL'
        value_to_symbol_dict[90] = 'XC'
        value_to_symbol_dict[400] = 'CD'
        value_to_symbol_dict[900] = 'CM'

        digits_stack = []
        original_number = num
        while (original_number):
            digit = original_number % 10
            digits_stack.append(digit)
            original_number = int(original_number/10)

        equivalent_roman_rep = ''
        pow_ten_multiplier = len(digits_stack) - 1
        while(digits_stack):
            current_digit = digits_stack.pop()
            current_digit = current_digit * int(pow(10,pow_ten_multiplier))
            pow_ten_multiplier -= 1
            if current_digit in value_to_symbol_dict:
                equivalent_roman_rep = equivalent_roman_rep + value_to_symbol_dict[current_digit]
            else:
                if current_digit % 1000 == 0:
                    for i in range(int(current_digit/1000)):
                        equivalent_roman_rep = equivalent_roman_rep + value_to_symbol_dict[1000]

                elif current_digit > 500 and current_digit < 900:
                    equivalent_roman_rep = equivalent_roman_rep + value_to_symbol_dict[500]
                    current_digit = current_digit - 500
                    for i in range(int(current_digit/100)):
                        equivalent_roman_rep = equivalent_roman_rep + value_to_symbol_dict[100]

                elif current_digit > 100 and current_digit < 400:
                    for i in range(int(current_digit/100)):
                        equivalent_roman_rep = equivalent_roman_rep + value_to_symbol_dict[100]

                elif current_digit > 50 and current_digit < 90:
                    equivalent_roman_rep = equivalent_roman_rep + value_to_symbol_dict[50]
                    current_digit = current_digit - 50
                    for i in range(int(current_digit/10)):
                        equivalent_roman_rep = equivalent_roman_rep + value_to_symbol_dict[10]

                elif current_digit > 10 and current_digit < 40:
                    for i in range(int(current_digit/10)):
                        equivalent_roman_rep = equivalent_roman_rep + value_to_symbol_dict[10]

                elif current_digit > 5 and current_digit < 9:
                    equivalent_roman_rep = equivalent_roman_rep + value_to_symbol_dict[5]
                    current_digit = current_digit - 5
                    for i in range(int(current_digit)):
                        equivalent_roman_rep = equivalent_roman_rep + value_to_symbol_dict[1]

                elif current_digit > 1 and current_digit < 4:
                    for i in range(int(current_digit)):
                        equivalent_roman_rep = equivalent_roman_rep + value_to_symbol_dict[1]

        return equivalent_roman_rep
if __name__ =="__main__":
    a = 3879
    soln = Solution()
    print(soln.intToRoman(a))