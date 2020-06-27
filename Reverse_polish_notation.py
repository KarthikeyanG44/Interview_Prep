# https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Input

# 4 2 3 + *

# 4 * (2+3)


# "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"

# 10 * {6 / [(9+3)* -11 ] } + 17 + 5
# 10 * {6/[-132]} + 17 + 5
# 10 * {0} + 17 + 5
# 0 + 17 + 5
# 22
# input will be a valid expression


def evaluate_RPN(tokens):
    if not tokens:
        return None

    evaluation_stack = []

    operator_map = ['+', '-', '*', '/']

    #     def is_number(token):
    #         return token.isdigit()

    #     def is_operand(token):
    #         token in operator_map

    for token in tokens:
        if token not in operator_map:
            equivalent_num = int(token)
            evaluation_stack.append(equivalent_num)
        else:
            num1 = evaluation_stack.pop()
            num2 = evaluation_stack.pop()
            if token == '+':
                expression_result = num1 + num2
            elif token == '-':
                expression_result = num1 - num2
            elif token == '*':
                expression_result = int(num1 * num2)
            elif token == '/':
                expression_result = int(num2 / num1)

            evaluation_stack.append(expression_result)

    return evaluation_stack[0]


print(evaluate_RPN(["2", "1", "/"]))
print(evaluate_RPN(["2", "1", "+", "3", "*"]))
print(evaluate_RPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))


"findneedleinahaystack"
O(M)

"needle"
O(N)




