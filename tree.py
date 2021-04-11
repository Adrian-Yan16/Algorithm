class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        # 之字形打印
        if not pRoot:
            return
        if not pRoot.left and not pRoot.right:
            return pRoot.val
        flag = True
        last = pRoot
        temp_list = [pRoot]
        res = []
        row = []
        next = None
        while temp_list:
            if flag:
                temp = temp_list.pop()
                row.append(temp.val)
                if temp.left:
                    temp_list.insert(0,temp.left)
                    if not next:
                        next = temp.left
                if temp.right:
                    temp_list.insert(0,temp.right)
                    if not next:
                        next = temp.right
                if temp == last:
                    res.append(row)
                    row = []
                    last = next
                    next = None
                    flag = not flag
            else:
                temp = temp_list.pop(0)
                row.append(temp.val)
                if temp.right:
                    temp_list.append(temp.right)
                    if not next:
                        next = temp.right
                if temp.left:
                    temp_list.append(temp.left)
                    if not next:
                        next = temp.left
                if temp == last:
                    res.append(row)
                    row = []
                    last = next
                    next = None
                    flag = not flag
        return res

    def pre(self,root):
        if not root:
            return
        temp_list = []
        temp = root
        res = []
        while temp_list or temp:
            while temp:
                temp_list.append(temp)
                res.append(temp.val)
                temp = temp.left
            temp = temp_list.pop()
            temp = temp.right
        return res


    def mid(self,root):
        temp_list = []
        temp = root
        res = []
        while temp_list or temp:
            while temp:
                temp_list.append(temp)
                temp = temp.left
            temp = temp_list.pop()
            res.append(temp.val)
            temp = temp.right
        return res

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

    def row(self,pRoot):
        if not pRoot:
            return
        if not pRoot.left and not pRoot.right:
            return [[pRoot.val]]
        temp_list = [pRoot]
        res = []
        last = pRoot
        row = []
        next = None
        while temp_list:
            temp = temp_list.pop(0)
            row.append(temp.val)
            if temp.left:
                temp_list.append(temp.left)
                next = temp.left
            if temp.right:
                temp_list.append(temp.right)
                next = temp.right
            if temp == last:
                res.append(row)
                last = next
                row = []
        return res

    def maxdepth(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.maxdepth(root.left)
        right = self.maxdepth(root.right)
        if left > right:
            return left + 1
        else:
            return right + 1

    def maxdepth2(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        temp_list = [root]
        count = 0
        while temp_list:
            temp = []
            for node in temp_list:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            temp_list = temp
            count += 1
        return count

    def maxdepth3(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        temp_list = [root]
        count = 0
        last = root
        next = None
        while temp_list:
            temp = temp_list.pop(0)
            if temp.left:
                temp_list.append(temp.left)
                next = temp.left
            if temp.right:
                temp_list.append(temp.right)
                next = temp.right
            if temp == last:
                last = next
                count += 1
        return count

    def path(self,root):
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        temp_list = [(root,[root.val])]
        res = []
        while temp_list:
            temp,temp_path = temp_list.pop(0)
            if not temp.left and not temp.right:
                res.append(temp_path)
            if temp.left:
                temp_list.append((temp.left,temp_path + [temp.left.val]))
            if temp.right:
                temp_list.append((temp.right,temp_path + [temp.right.val]))
        return res

    def depth_searach(self,root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        temp_list = [root]
        res = []
        while temp_list:
            temp = temp_list.pop()
            res.append(temp.val)
            if temp.right:
                temp_list.append(temp.right)
            if temp.left:
                temp_list.append(temp.left)
        return res

    def min_depth(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        temp_list = [root]
        count = 1
        while temp_list:
            temp = []
            for node in temp_list:
                if not node.left and not node.right:
                    return count
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            temp_list = temp
            count += 1
        return count

    def Serialize(self, root):
        # write code here
        if not root:
            return '#!'
        if not root.left and not root.right:
            return '%d!' % root.val
        temp_list = []
        temp = root
        res = ''
        while temp or temp_list:
            while temp:
                temp_list.append(temp)
                res += str(temp.val) + '!'
                temp = temp.left
                if not temp:
                    res += '#!'
            temp = temp_list.pop()
            temp = temp.right
            if not temp:
                res += '#!'
        return res

    flag = -1
    def Deserialize(self, s):
        if not s:
            return
        self.flag += 1
        l = s.split('!')[:-1]
        if self.flag >= len(l):
            return
        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root





if __name__ == '__main__':
    tree1 = TreeNode(5)
    # tree1.left = TreeNode(2)
    # tree1.right = TreeNode(3)
    # tree1.left.left = TreeNode(4)
    # tree1.left.left.left = TreeNode(8)
    # tree1.left.right = TreeNode(5)
    # tree1.right.left = TreeNode(6)
    # tree1.right.right = TreeNode(7)
    s = Solution()
    # print(s.Serialize2(tree1))
    r = s.Serialize(tree1)
    print(s.Serialize(tree1))
    print(s.Deserialize(r).val)














