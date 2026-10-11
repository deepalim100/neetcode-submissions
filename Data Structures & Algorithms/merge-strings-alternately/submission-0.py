class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l_w1, l_w2 = 0, 0
        r_w1 , r_w2 = len(word1), len(word2)
        res = ""
        while l_w1 < r_w1 and l_w2 < r_w2:
            res += word1[l_w1] + word2[l_w2]
            l_w1 += 1
            l_w2 += 1

        while l_w1 < r_w1:
            res += word1[l_w1]
            l_w1 += 1
        while l_w2 < r_w2:
            res += word2[l_w2]
            l_w2 += 1

        return res
        