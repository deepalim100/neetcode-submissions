class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            # print(s, type(s), type(sorted(s)))
            if str(sorted(s)) in dict:
                print("".join(sorted(s)))
                dict[str(sorted(s))].append(s)
            else:
                dict[str(sorted(s))] = [s]

        fin_list = list(dict.values())

        return fin_list

