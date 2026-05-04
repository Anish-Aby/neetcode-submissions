class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minWord = min(strs)
        
        for word in strs:
            commonPrefix = ""
            for i in range(len(minWord)):
                if minWord[i] != word[i]:
                    minWord = commonPrefix
                    break
                commonPrefix += minWord[i]
        
        return minWord