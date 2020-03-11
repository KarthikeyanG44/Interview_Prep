class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s and not t or not s and t:
            return False
        if len(s) != len(t):
            return False
        if len(s) == len(t) and len(s) == 1:
            return s == t

        string_1_dict = {}
        string_2_dict = {}

        for char_1 in s:
            if char_1 in string_1_dict:
                temp = string_1_dict[char_1]
                string_1_dict[char_1] = temp + 1
            else:
                string_1_dict[char_1] = 1

        for char2 in t:
            if char2 in string_2_dict:
                temp = string_2_dict[char2]
                string_2_dict[char2] = temp + 1
            else:
                string_2_dict[char2] = 1

        l1 = [(key, value) for key, value in string_1_dict.items()]
        l2 = [(key, value) for key, value in string_2_dict.items()]

        return l1 == l2