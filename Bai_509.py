class Solution:
    def fib(self, n: int) -> int:
        f0 = 0
        f1 = 1
        fn = 1
        if (n < 0):
            return -1
        elif (n == 0 or n == 1):
            return n
        else:
            for i in range(2, n):
                f0 = f1
                f1 = fn
                fn = f0 + f1
            return fn
