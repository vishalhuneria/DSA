class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def find( n , sum):
            if n == 0 :
                if sum == target : return 1
                else: return 0
            if (n , sum ) in dp :
                return dp[(n, sum)]
            
            add = find( n -1 , sum +nums[n-1])
            subtract = find(n-1 , sum  - nums[n-1])

            dp[(n , sum )]= add + subtract
            return dp[(n , sum )]
        return  find(len(nums) , 0)