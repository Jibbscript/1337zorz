class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str, memo: dict = {}) -> bool:
        if len(s1) + len(s2) is not len(s3):
            return False
        if not s1 and not s2 and not s3:
            return True
        if (s1,s2,s3) in memo:
            return memo[(s1,s2,s3)]
        if (s1,s2,s3) not in memo:
        
            s1check = (s1 and s1[0] == s3[0]) and self.isInterleave(s1[1:],s2,s3[1:])
        
            s2check = (s2 and s2[0] == s3[0]) and self.isInterleave(s1,s2[1:],s3[1:])
            
            memo[(s1,s2,s3)] = s1check or s2check
        return memo[(s1,s2,s3)]
