"""
leetcode 818 Race Car


Your car starts at position 0 and speed +1 on an infinite number line.  
Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions 
A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: 
position += speed, speed *= 2.

When you get an instruction "R", your car does the following: 
if your speed is positive then speed = -1 , otherwise speed = 1.  
(Your position stays the same.)

For example, after commands "AAR", your car goes to positions 
0->1->3->3, and your speed goes to 1->2->4->-1.

"""

class Solution(object):

    dp = {0: 0}
    def racecar(self, t):
        """
        :type target: int
        :rtype: int
        """
        

        if t in self.dp:
            return self.dp[t]

        n = t.bit_length()
        
        if 2**n - 1 == t:
            self.dp[t] = n
        else:
            self.dp[t] = self.racecar(2**n - 1 - t) + n + 1
            for m in range(n - 1):
                self.dp[t] = min(self.dp[t], self.racecar(t - 2**(n - 1) + 2**m) + n + m + 1)
        
        return self.dp[t]