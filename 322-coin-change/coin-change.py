class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = {}
        def find( sum ):
            if sum < 0 :  return float("inf")
            if sum == 0:
                return 0
            if sum in dp:
                return dp[sum]
            ans  = float("inf")
            for i in coins :
                ans = min(ans  ,1 + find( sum  - i) )
            
            dp[sum] = ans
            return ans 
        
        ans  = find(amount )
        return   ans if ans != float("inf") else -1 
