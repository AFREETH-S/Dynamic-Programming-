class Solution:
    def climbStairs(self, n: int) -> int:
        a={1:1,2:2,3:3}
        for i in range(4,n+1):
            a[i]=a[i-1]+a[i-2]
        return a[n]
