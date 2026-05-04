class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLen, tLen = len(s), len(t)
         
        if sLen != tLen:
            return False

        return Counter(s) == Counter(t)