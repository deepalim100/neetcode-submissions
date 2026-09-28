class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s , t = set(list(s)), set(list(t))
        print(s , t)
        return s == t