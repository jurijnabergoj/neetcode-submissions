class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            prefix = str(len(s)) + "#"
            encoded_str += (prefix + s)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        decoded_str = ""
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            result.append(s[j+1:j+length+1])
            i = j + length + 1
        return result