#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
class Solution:
    # Your runtime beats 43.24 % of python3 submissions
    def countAndSay(self, n: int) -> str:
        result = '1'
        for _ in range(n-1):
            prev = result
            result = ''
            j = 0
            while j <len(prev):
                curr = prev[j]
                cnt =1
                j +=1
                while j<len(prev) and prev[j] == curr:
                    j+=1
                    cnt+=1
                result +=str(cnt) + str(curr)
        return result


