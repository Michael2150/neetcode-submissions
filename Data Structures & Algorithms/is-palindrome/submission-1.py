class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [l.lower() for l in s if l.isalnum()] 
        y = x[::-1] 
        return x == y