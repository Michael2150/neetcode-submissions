class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()

        for x in s:
            if x in letters:
                letters[x] += 1
            else:
                letters[x] = 1

        for y in t:
            if y in letters:
                letters[y] -= 1
            else:
                return False
        
        for z in letters:
            if letters[z] != 0:
                return False
            
        return True