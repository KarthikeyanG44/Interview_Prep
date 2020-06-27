def backspaceCompare(S, T):
    if not T or not S:
        return False

    string_1_stack = []
    string_2_stack = []

    for symbol1 in S:
        if symbol1 == '#' and string_1_stack:
            string_1_stack.pop()
        elif symbol1 == '#' and not string_1_stack:
            continue
        else:
            string_1_stack.append(symbol1)

    for symbol2 in T:
        if symbol2 == '#' and string_2_stack:
            string_2_stack.pop()
        elif symbol2 == '#' and not string_2_stack:
            continue
        else:
            string_2_stack.append(symbol2)

    print(string_1_stack,string_2_stack)
    return string_1_stack == string_2_stack
if __name__=="__main__":
    s1 = "ab#c"
    s2 = "ad#c"
    compare = backspaceCompare(s1,s2)
    print(compare)