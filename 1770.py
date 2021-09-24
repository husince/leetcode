class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        len_nums, dp = len(nums), [0] * (len(multipliers) + 1)

        for index, m in enumerate(multipliers):
            len_remain = len_nums - index - 1

            dp[len_nums - len_remain] = dp[len_nums - len_remain - 1] + m * nums[len_nums - len_remain - 1]

            for j in range(len_nums - len_remain - 1, 0, -1):
                dp[j] = max(
                    dp[j  ] + m * nums[j + len_remain],
                    dp[j-1] + m * nums[j - 1],
                )

            dp[0] += m * nums[len_remain]

        return max(dp)