from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s , t = Counter(s), Counter(t)
        print(s , t)
        return s == t