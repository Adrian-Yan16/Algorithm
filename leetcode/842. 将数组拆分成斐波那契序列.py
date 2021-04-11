class Solution:
    # 回溯
    def splitIntoFibonacci(self, S: str):
        length = len(S)
        res = []
        def backtrack(pos):
            # 基线条件
            if pos == length:
                return len(res) > 2
            s = 0
            for i in range(pos,length):
                s = s * 10 + int(S[i])
                # 剪枝条件1：数值不大于 int 最大值
                if s > 2 ** 31 - 1:
                    break
                # 剪枝条件2：当前值大于前两项和
                if len(res) >= 2 and res[-1] + res[-2] < s:
                    break
                # 剪枝条件3：首位为 0，但值不为 0
                if S[pos] == '0' and i > pos:
                    break
                if len(res) < 2 or res[-1] + res[-2] == s:
                    res.append(s)
                    if backtrack(i + 1):
                        return True
                    res.pop()
            return False
        return res if backtrack(0) else []











s = Solution()
S = "1101111"
# S = "11235813"
# S =  "112358130"
# S = "0123"
S = "123456579"
# S = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
S = "3611537383985343591834441270352104793375145479938855071433500231900737525076071514982402115895535257195564161509167334647108949738176284385285234123461518508746752631120827113919550237703163294909"
res = s.splitIntoFibonacci(S)
print(res)

