class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [l.lower() for l in s if l.isalnum()]
        if len(s)<=1:
            return True
        if s[0]==s[-1]:
            return self.isPalindrome(s[1:-1])
        else:
            return False