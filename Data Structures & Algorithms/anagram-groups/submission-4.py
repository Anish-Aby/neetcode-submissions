class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def getStrArr(word):
            arr = [0] * 26
            for letter in word:
                arr[ord(letter) - ord('a')] += 1
            return arr

        res = defaultdict(list)
        for word in strs:
            strArr = getStrArr(word)
            res[tuple(strArr)].append(word)
            
        return list(res.values())