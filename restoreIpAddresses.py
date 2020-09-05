# Given a string s containing only digits. Return all possible valid IP addresses that can be obtained from s. You can return them in any order.

# A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single points and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]

# Example 3:

# Input: s = "1111"
# Output: ["1.1.1.1"]

# Example 4:

# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]

# Example 5:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

 

# Constraints:

#     0 <= s.length <= 3000
#     s consists of digits only.

import re

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        p = re.compile('^0[0-9]+')
        result = []
        for i in range(1,len(s)-2):
            a = s[0:i]
            if(int(a) > 255 or p.match(a)):
                break
            for j in range(i+1,len(s)-1):
                b = s[i:j]
                if(int(b) > 255 or i >= j or p.match(b)):
                    break
                for k in range(j+1,len(s)):
                    c = s[j:k]
                    if(int(c) > 255 or j >= k or p.match(c)):
                        break
                    d = s[k:len(s)]
                    if(int(d) <= 255 and not p.match(d)):
                        result.append(a+"."+b+"."+c+"."+d)
        return result