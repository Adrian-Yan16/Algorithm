class TreeNode():
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    def rob(self, nums) -> int:
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums)
        for i in range(2,l):
            if nums[:i-2]:
                nums[i] += max(nums[:i-1])
            else:
                nums[i] += nums[i - 2]
        return max(nums)

    def rob2(self,nums):
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums)
        def rob(nums):
            cur,pre = 0,0
            for i in nums:
                cur,pre = max(pre+i,cur),cur
            return cur
        return max(rob(nums[1:]),rob(nums[:-1]))

    def rob3_rec(self,root):
        def dfs(root):
            if not root:
                return 0,0
            left = dfs(root.left)
            right = dfs(root.right)
            v1 = left[1] + right[1] + root.val
            v2 = max(left) + max(right)
            return v1,v2
        return max(dfs(root))

    # def rob3_dp(self,root):
    #     def dfs(root):


tree1 = TreeNode(3)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
# tree1.left.left = TreeNode(3)
# tree1.left.left.left = TreeNode(2)
tree1.left.right = TreeNode(3)
# tree1.right.left = TreeNode(6)
tree1.right.right = TreeNode(1)
s = Solution()
print(s.rob3_rec(tree1))