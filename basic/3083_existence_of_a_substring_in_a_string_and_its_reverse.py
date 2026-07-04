class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reversed_s = s[::-1]
        hash_map = {}
        
        for i in range(len(s) - 1):
            sub = s[i] + s[i+1]
            
            if sub not in hash_map:
                hash_map[sub] = 0
        
        for i in range(len(s) - 1):
            sub = reversed_s[i] + reversed_s[i+1]
            if sub in hash_map:
                return True
        
        return False
