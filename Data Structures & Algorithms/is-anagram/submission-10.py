from sympy import primerange
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        primes = list(primerange(0, 102))
        map = {}
        for i, prime in zip(range(26), primes):
            ch = chr(97 + i)
            map[ch] = prime
        
        s_num = 1
        t_num = 1

        for c1, c2 in zip(s, t):
            s_num *= map[c1]
            t_num *= map[c2]
        
        return s_num == t_num


