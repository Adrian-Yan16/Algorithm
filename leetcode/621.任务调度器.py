from collections import Counter

# 时间及空间复杂度均为O(n)
class Solution:
    def leastInterval(self, tasks,n: int) -> int:
        length = len(tasks)
        d = Counter(tasks)
        vals = list(d.values())
        # 得到任务数最多任务数量
        max_count = max(vals)
        # 最后一次执行该任务之前的执行时间
        # AAABBCC,n == 2
        # (A__A__)A
        res = (max_count - 1) * (n + 1)
        # 最后一个A及之后的要执行的任务为与A任务数相同的任务
        res += vals.count(max_count)
        # 当n==0时，时间等于任务数
        return max(length,res)


s = Solution()
print(s.leastInterval(tasks = ["A","A","A","B","B","C","C","D","D"], n = 2))
