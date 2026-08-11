class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1

        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1


        for i in range(3, n+1):
            if a <= b and a <= c:
                a = a + b + c
            elif b <= a and b <= c:
                b = a + b + c
            else:
                c = a + b + c
        
        return max(a, b , c)
