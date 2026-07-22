class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l, n = 0, len(s2)
        n_s1 = len(s1)

        while l < n:
            n_s2 = s2[l:l+n_s1]
            if sorted(list(n_s2)) == sorted(list(s1)):
                return True
            else:
                l += 1
        return False
        