class Solution:
    dp = [-1] * 31

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        # Temporary variables to store values of fib(n-1) & fib(n-2)
        first = self.dp[n - 1] if self.dp[n - 1] != -1 else self.fib(n - 1)
        second = self.dp[n - 2] if self.dp[n - 2] != -1 else self.fib(n - 2)

        # Memoization
        self.dp[n] = first + second
        return self.dp[n]