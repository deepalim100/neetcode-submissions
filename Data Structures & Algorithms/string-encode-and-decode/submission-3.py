class Solution:

    def encode(self, strs: List[str]) -> str:
        res_str = ''
        for i in strs:
            res_str += str(len(i))+'#'+i
        return res_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            num = int(s[i:j])
            i = j + 1
            word = s[i:i+num]
            i += num
            res.append(word)
        return res
