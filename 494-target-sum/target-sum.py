class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if total < abs(target):
            return 0

        if (total + target) % 2 != 0:
            return 0

        tar = (total + target) // 2

        dp = [0] * (tar + 1)
        dp[0] = 1

        for num in nums:
            for s in range(tar, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[tar]