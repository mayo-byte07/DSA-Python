class Solution(object):
    def minFlips(self, a, b, c):
        flips = 0
        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            if bit_c == 1:
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            else:
                flips += (bit_a + bit_b)
            a >>= 1
            b >>= 1
            c >>= 1
            
        return flips