class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstString = {}
        secondString = {}
        for char in s:
            if char not in firstString:
                firstString[char] = 1
            else:
                firstString[char]+=1
        
        for char in t:
            if char not in secondString:
                secondString[char] = 1
            else:
                secondString[char]+=1
        
        for key in firstString.keys():
            if key not in secondString or len(firstString)!=len(secondString) or firstString[key] != secondString[key]:
                return False
        return True