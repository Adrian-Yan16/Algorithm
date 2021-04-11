class Solution:
    def combinationSum_back(self, candidates, target: int):
        candidates.sort()
        res = []
        def find(s,use,remain):
            for i in range(s,len(candidates)):
                c = candidates[i]
                if c == remain:
                    res.append(use + [c])
                    return
                elif c < remain:
                    find(i,use + [c],remain - c)
                else:
                    return
        find(0,[],target)
        return res

    def combinationSum2_back(self, candidates, target: int):
        candidates.sort()
        res = []

        def find(s, use, remain):
            for i in range(s, len(candidates)):
                if i > s and candidates[i] == candidates[i - 1]:
                    continue
                c = candidates[i]
                if c == remain:
                    res.append(use + [c])
                    return
                elif c < remain:
                    find(i + 1, use + [c], remain - c)
                else:
                    return

        find(0, [], target)
        return res

    def combinationSum3_back(self,k , n: int):
        res = []

        def find(s, use, remain):
            for i in range(s, 10):
                if i == remain:
                    if len(use + [i]) == k:
                        res.append(use + [i])
                    return
                elif i < remain:
                    find(i + 1, use + [i], remain - i)
                else:
                    return

        find(1, [], n)
        return res

    def combinationSum4_back(self, nums, target: int) -> int:
        # 超时
        self.res = 0

        def find(remain):
            for i in range(len(nums)):
                c = nums[i]
                if c == remain:
                    self.res += 1
                elif c < remain:
                    find(remain - c)

        find(target)
        return self.res

    def combinationSum4_dp(self, nums, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1,target + 1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i - j]
        return dp[-1]






s = Solution()
print(s.combinationSum4_dp([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],10))