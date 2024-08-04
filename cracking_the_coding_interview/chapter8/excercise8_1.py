class Solution:

    def __init__(self):
        pass

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        memo = [0, 1, 1]
        a = 0
        b = 1
        c = 1
        for i in range(n-2):
            #memo.append(memo[i]+memo[i+1]+memo[i+2])
            a, b, c = b, c, a+b+c
        #return memo[-1]
        return c

    def tribonacci2(self, n: int) -> int:
        self.memo = [0, 1, 1]
        return self.rec(n)

    def rec(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if len(self.memo) <= n:
            self.memo.append(self.rec(n-1)+self.rec(n-2)+self.rec(n-3))
        return self.memo[n]


s = Solution()
print(s.tribonacci(3))
print(s.tribonacci(4))
print(s.tribonacci(25))

print(s.tribonacci2(3))
print(s.tribonacci2(4))
print(s.tribonacci2(25))