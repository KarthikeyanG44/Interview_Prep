def findSumPair(a,b,sum):
    pair_list = []
    a = [int(x) for x in a.split(',')]
    b = [int(y) for y in b.split(',')]
    res_dict = {}
    for val in b:
        res_dict[val] = val

    for first_num in a:
        residual = sum - first_num
        if residual in res_dict:
            pair_list.append((first_num,residual))

    return pair_list

if __name__=="__main__":
    list1 = input("Enter first list")
    list2 = input("Enter second list")
    target = int(input("Enter sum"))
    pairs = findSumPair(list1,list2,target)
    for pair in pairs:
        print(pair)