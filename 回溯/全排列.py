def permute(nums):
    result = []
    # track 代表路径
    track = []

    def backtrack(nums,track):
        # 结束条件：如果nums中的数字都出现在了 track中，循环终止
        if len(track) == len(nums) and track not in result:
            result.append(track.copy())
            return
        for num in nums:
            if num in track:
                continue
            # 选择列表：选择在nums中但track中还没有的数字
            track.append(num)
            # 撤销选择
            backtrack(nums,track)
            track.pop()
    backtrack(nums,track)
    return result


p = permute([1,2,3])
print(p)