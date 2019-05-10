#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        
        isNotPrime = [False] * n
        cnt=0
        for i in range(2,n):
            if isNotPrime[i] == False:
                cnt+=1
                for j in range(2,n):
                    if i*j>=n:
                        break
                    isNotPrime[i*j] = True           
        
        return cnt


        '''
        def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        res = 0
        not_prime = [False] * n

        for i in range(2, n):
            if not_prime[i] == False:
                res += 1
                for j in range(2, n):
                    if j * i >= n:
                        break
                    not_prime[j * i] = True
        return res
        '''


        

