"""
leetcode 455. Assign Cookies

Assume you are an awesome parent and want to give your children 
some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of 
a cookie that the child will be content with; and each cookie j 
has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the 
child i, and the child i will be content. Your goal is to maximize 
the number of your content children and output the maximum number.

"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()
        i = 0
        res = 0
        
        for item in g:
            while i < len(s) and s[i] < item:
                i += 1
            if i < len(s) and s[i] >= item:
                res += 1
                i += 1
        return res