class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        l = len(s)
        dp = [False] * (l + 1)
        dp[0] = True
        for i in range(1,l+1):
            for j in range(i - 1,-1,-1):
                temp = s[j:i]
                if dp[j] and temp in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

    def wordBreak2(self, s: str, wordDict) -> bool:
        l = len(s)
        dp = [0]
        for i in range(1,l+1):
            for j in range(i - 1, -1, -1):
                if (j in dp) and s[j:i] in wordDict:
                    dp.append(i)
                    break
        return dp[-1] == l

s = Solution()
print(s.wordBreak2(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))