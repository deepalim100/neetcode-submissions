class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win_set = set()
        l , r, max_len = 0,0,0
        while r < len(s):
            if s[r] not in win_set:
                win_set.add(s[r])
            else:
                while s[r] in win_set:
                    win_set.remove(s[l])
                    l += 1  
                win_set.add(s[r]) 
            max_len = max(max_len, len(win_set))
            r += 1
        return max_len
        