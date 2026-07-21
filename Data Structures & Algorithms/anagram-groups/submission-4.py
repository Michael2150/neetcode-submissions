class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []

        for x in strs: #Each of the strings
            isGrouped = False
            for g in groups: #Check the groups 
                if sorted(x) == sorted(g[0]):
                    isGrouped = True
                    g.append(x)
            if isGrouped == False:
                groups.append([x])

        return groups
    