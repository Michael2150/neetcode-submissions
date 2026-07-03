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
        
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for ch in s:
            letters[ch] = letters.get(ch, 0) + 1

        for ch in t:
            if ch not in letters:
                return False
            letters[ch] -= 1

        return all(v == 0 for v in letters.values())