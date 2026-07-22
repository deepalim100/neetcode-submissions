class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_group = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagram_group:
                anagram_group[sorted_str].append(s)
            else:
                anagram_group[sorted_str] = [s]
        return anagram_group.values()
        