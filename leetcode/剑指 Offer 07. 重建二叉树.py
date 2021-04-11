# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder and not inorder:
            return None
        if len(preorder) != len(inorder):
            return TreeNode(None)
        root_val = preorder[0]
        idx = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:idx + 1],inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:],inorder[idx + 1:])
        return root

    # 迭代
    def buildTree1(self, preorder, inorder) -> TreeNode:
        l = len(preorder)
        if l == 0:
            return None
        table = {}
        for i,x in enumerate(inorder):
            table[x] = i
        # 下一个要操作的节点
        cur = 1
        root = TreeNode(preorder[0])
        stack = [root]
        while cur < l:
            previous_node = stack[-1]
            cur_node = TreeNode(preorder[cur])

            # 判断当前节点在中序遍历中在上一个节点的前面还是后面
            if table[cur_node.val] < table[previous_node.val]:
                previous_node.left = cur_node
            else:
                # 将栈中元素连续出栈直到栈为空或者栈顶元素在中心遍历在在当前节点的前面
                while stack and table[cur_node.val] > table[stack[-1].val]:
                    previous_node = stack.pop()
                # 此时当前节点为该节点的右子节点
                previous_node.right = cur_node
            stack.append(cur_node)
            cur += 1
        return root






















