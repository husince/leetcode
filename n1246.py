class Solution(object):
    # https://nagato1208.github.io/2019/11/02/leetcode-1246-Palindrome-Removal/
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = [[100] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if j == n:
                    break
                dp[i][j] = 1 + (dp[i + 1][j] if i + 1 < n else 0)
                for k in range(i + 1, j + 1):
                    if arr[i] == arr[k]:
                        if k == i + 1:
                            dp[i][j] = min(dp[i][j], 1 + (dp[k + 1][j] if k + 1 <= j else 0))
                        else:
                            dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + (dp[k + 1][j] if k + 1 <= j else 0))
        return dp[0][n - 1]

class Solution2:
    # https://www.youtube.com/watch?v=KxvTeK2nv28
    # https://pastebin.com/HW750Epx
    def minimumMoves(self, arr):
        n = len(arr)
        dp = [[n for _ in range(n)] for _ in range(n)]
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if l == r:
                    dp[l][r] = 1
                elif l + 1 == r:
                    dp[l][r] = 2
                    if arr[l] == arr[r]:
                        dp[l][r] = 1
                else:
                    dp[l][r] = min(
                        dp[l + 1][r - 1] + (0 if arr[l] == arr[r] else 2),
                        dp[l][r], dp[l + 1][r] + 1,
                        dp[l][r - 1] + 1)
                    for k in range(l, r):
                        dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r])
        return dp[0][n - 1]