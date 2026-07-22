from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s , count_t = {}, {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        for char in t:
            if char not in count_s or count_s[char] == 0:
                return False
            count_t[char] = count_t.get(char, 0) + 1 
        
        return count_t == count_s