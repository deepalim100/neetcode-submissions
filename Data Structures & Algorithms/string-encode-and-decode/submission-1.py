class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return strs
        return '#'.join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return s
        return s.split('#')