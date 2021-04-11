import copy


class Solution:
    def lemonadeChange(self, bills) -> bool:
        length = len(bills)
        if bills[0] != 5:
            return False
        bills_copy = copy.deepcopy(bills)
        dp = [0] * length
        dp[0] = 1
        k = 0
        for i in range(1,length):
            s = 0
            if bills[i] == 5:
                dp[i] = 1
            else:
                for j in range(k,i):
                    
                    temp = sorted(bills[k:i])
                    s += temp[j]
                    if bills[i] - s == 5:
                        k = j + 1
                        dp[i] = 1
                        temp.pop(i)
                        break
        return dp[-1] == 1


s = Solution()
bills =[5,5,5,10,20]
print(s.lemonadeChange(bills))
