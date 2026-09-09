from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_str1 =  {}
        for i in s:
            if i in dict_str1:
                dict_str1[i] += 1
            else:
                dict_str1[i] = 1

        for i in t:
            dict_str1[i] = dict_str1.get(i, 0) - 1

        return all(value == 0 for value in dict_str1.values())