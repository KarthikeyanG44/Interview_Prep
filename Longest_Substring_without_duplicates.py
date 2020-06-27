def lengthOfLongestSubstring(s):
    if not s:
        return 0

    last_seen_dict = {}
    start_idx = 0
    longest = [0, 1]

    for i, c in enumerate(s):
        if c in last_seen_dict:
            start_idx = max(start_idx, last_seen_dict[c] + 1)
        if longest[1] - longest[0] < i + 1 - start_idx:
            longest = [start_idx, i + 1]
        last_seen_dict[c] = i

    return longest[1] - longest[0]
if __name__=="__main__":
    str1 = "pwwkew"
    longest_substring = lengthOfLongestSubstring(str1)
    print(longest_substring)