def coin_change(coins,amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1,amount + 1):
        for coin in coins:
            if i < coin:
                break
            dp[i] = min(dp[i],dp[i - coin] + 1)
    if dp[-1] == amount + 1:
        return -1
    return dp[-1]

c = coin_change([1,2,5],11)
print(c)