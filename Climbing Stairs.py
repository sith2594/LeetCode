# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# 1 <= n <= 45
class Solution:
    def climbStairs(self, n: int) -> int:
        i = 0
        sum = 0
        while(n - 2 * i >= 0):
            h = n - 2 * i
            sum = sum + math.factorial(h+i)/(math.factorial(i) * math.factorial(h))
            i = i + 1
        return int(sum)
