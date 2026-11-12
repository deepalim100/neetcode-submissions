class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq , win_freq = {}, {}
        l = 0
        for i in s1:
            s1_freq[i] = s1_freq.get(i, 0) + 1
        
        for r in range(len(s2)):
            win_freq[s2[r]] = win_freq.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                win_freq[s2[l]] -= 1
                if win_freq[s2[l]] == 0:
                    del win_freq[s2[l]]
                l += 1

            if win_freq == s1_freq:
                return True
        return False
        