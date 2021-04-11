class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minTrianglePath(self,triangle):
        dp = triangle[-1]
        for i in range(-2,-len(triangle) - 1,-1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j],dp[j + 1])
        return dp[0]

    def coinChange(self, coins, amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for j in coins:
            for i in range(j,amount + 1):
                dp[i] = min(dp[i],dp[i - j] + 1)
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]

    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        f0 = 1
        f1 = 1
        for _ in range(1, n):
            f0, f1 =f1, f1 + f0
        return f1 % 1000000007

    def spiralOrder(self, matrix):
        temp = matrix.pop(0)
        while matrix:
            matrix = list(zip(*matrix))[::-1]
            print(matrix)
            temp += matrix.pop(0)
        return temp


    def exist(self, board, word: str) -> bool:
        row = len(board)
        col = len(board[0])
        flag = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if self.judge(board,i,j,flag,word,0):
                    return True
                continue
        return False

    def judge(self,board,i,j,flag,word,k):
        row = len(flag)
        col = len(flag[0])
        if i < 0 or j < 0 or i >= row or j >= col or k >= len(word) or board[i][j] != word[k] or flag[i][j] == 1:
            return False
        if k == len(word) - 1 and board[i][j] == word[k]:
            return True
        flag[i][j] = 1
        if (self.judge(board,i + 1,j,flag,word,k + 1) or
            self.judge(board, i - 1, j, flag, word, k + 1) or
            self.judge(board, i, j + 1, flag, word, k + 1) or
            self.judge(board, i, j - 1, flag, word, k + 1)):
            return True
        flag[i][j] = 0
        return False

    def findRepeatNumber(self, nums) -> int:
        res = []
        for i in range(len(nums)):
            tmp = nums[i]
            if i != tmp:
                if tmp != nums[tmp]:
                    nums[i], nums[tmp] = nums[tmp], nums[i]
                else:
                    return nums[i]

    def buildTree(self, preorder, inorder) -> TreeNode:
        """
                迭代，用栈来保存元素。
                按照前序来生成结点，每个当前节点需要根据中序顺序判断其在上一节点（栈顶元素）的前还是后（构建哈希表加快查询）：
                1、当前元素是栈顶元素的中序顺序之前：连接二者，并把当前元素入栈。
                2、当前元素是栈顶元素的中序顺序之后：必须明确当前元素不一定是栈顶元素的左子节点，必须连续出栈直到栈顶元素在中序中的顺序比当前元素靠前，
                   此时最后出栈的元素的右子节点就是当前元素，连接二者，并把当前元素入栈。
                """
        if len(preorder) == 0:
            return None

        table = {}
        for i, x in enumerate(inorder):
            table[x] = i

        stack = []
        cur = 1
        root = TreeNode(preorder[0])
        stack.append(root)
        while cur < len(preorder):
            last_node = stack[-1]
            cur_node = TreeNode(preorder[cur])

            # 当前元素是栈顶元素的中序顺序之前
            if table[cur_node.val] < table[last_node.val]:
                last_node.left = cur_node

            # 当前元素是栈顶元素的中序顺序之后
            else:
                # 关键：连续出栈直到栈顶元素在中序中的顺序比当前元素靠前
                while stack and table[cur_node.val] > table[stack[-1].val]:
                    last_node = stack.pop()

                last_node.right = cur_node

            stack.append(cur_node)  # 不管怎样都要入栈
            cur += 1

        return root

    def last(self,root):
        temp_list = []
        temp = root
        res = []
        while temp_list or temp:
            while temp:
                temp_list.insert(0,temp)
                res.insert(0,temp.val)
                temp = temp.right
            temp = temp_list.pop(0)
            temp = temp.left
        return res





s = Solution()
tri = [[2],
       [3,4],
       [6,5,7],
       [4,1,8,9]]
# print(s.coinChange(coins = [186,419,83,408], amount = 6249))
# print(s.numWays(44))
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(s.spiralOrder(matrix))
# print(s.exist(board = [["a","b"],["c","d"]], word = "abcd"))
# print(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
root = s.buildTree(preorder = [3,9,20,15,7],inorder = [9,3,15,20,7])
print(s.last(root))