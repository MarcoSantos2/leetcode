# Encode and decode a list of strings
# Encode and Decode Strings
""" Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]"""

class Solution:
    def encode(self, strs: List[str]) -> str:
        
        s = ''
        for word in strs:
            s += str(len(word))+'#'+word
        print(s)
        return s

    def decode(self, s: str) -> List[str]:

        decoded = []
        i = 0
        while i < len(s):
            j = i
            for _ in range(len(s)):
                print("S OF J", s[j])
                if s[j] == '#':
                    print(s[i:j])
                    word_len = int(s[i:j])
                    decoded.append(str(s[j+1:j+1+word_len]))
                    i = j+1+word_len
                    break
                j+=1
            
        return decoded     