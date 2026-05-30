class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupList = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            groupList[key].append(i)
        
        return list(groupList.values())
             
            
        