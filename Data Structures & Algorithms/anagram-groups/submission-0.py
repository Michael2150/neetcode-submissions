class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []

        for x in strs: #Each of the strings
            isGrouped = False
            for g in groups: #Check the groups 
                group_word = g[0]
                if self.isAnagram(x, group_word):
                    isGrouped = True
                    g.append(x)
            if isGrouped == False:
                groups.append([x])

        return groups
        
    from collections import Counter

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)