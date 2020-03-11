def find_pairs_with_given_difference(arr, k):
    diff_array = []

    for val in arr:
        residual = val - k
        if residual in arr and [val, residual] not in diff_array:
            diff_array.append([val, residual])

    diff_array.sort(key=lambda x: arr.index(x[1]))
    return diff_array
