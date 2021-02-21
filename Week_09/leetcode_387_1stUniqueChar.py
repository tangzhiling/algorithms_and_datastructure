"""
leetcode 387. First Unique Character in a String

Given a string, find the first non-repeating character in it 
and return its index. If it doesn't exist, return -1.


"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        
        for i, char in enumerate(s):
            if dic[char] and dic[char] == 1:
                return i
        return -1