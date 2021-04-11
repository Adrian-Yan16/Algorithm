class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput:
            return
        if k > len(tinput):
            return tinput
        sort_list = self.heap_sort(tinput)
        return sort_list

    def quick_sort(self,list_):
        # 快排
        # 随机选择一个数字作为基准，将比其小的数字分到左边，比其大的数字分到右边
        left = []
        right = []
        mid_num = list_.pop()
        for i in list_:
            if i < mid_num:
                left.append(i)
            else:
                right.append(i)
        return self.quick_sort(left) + [mid_num] + self.quick_sort(right)

    def merge_sort(self,list_):
        # 归并排序
        # 将数组分为两份，然后对每一份进行排序，返回排序后的数组，进行合并
        if len(list_)<=1:
            return list_
        mid = len(list_) // 2
        left = self.merge_sort(list_[:mid])
        right = self.merge_sort(list_[mid:])
        return self.merge(left,right)

    def merge(self,left,right):
        if not left and not right:
            return []
        if not left:
            return right
        if not right:
            return left
        result = []
        while left and right:
            if left[0] >= right[0]:
                result.append(right.pop(0))
            else:
                result.append(left.pop(0))
        return result + left + right

    def heap_sort(self,list_):
        # 堆排序
        #堆是具有以下性质的完全二叉树：每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；
        # 或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆
        # 将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。
        # 将其与末尾元素进行交换，此时末尾就为最大值。然后将剩余n-1个元素重新构造成一个堆，
        # 这样会得到n个元素的次小值。如此反复执行，便能得到一个有序序列了
        if len(list_) <= 1:
            return list_
        length = len(list_)
        first = length // 2 - 1
        for start in range(first,-1,-1):
            self.build_heap(list_,start,length - 1)
        for end in range(length - 1,0,-1):
            list_[0],list_[end] = list_[end],list_[0]
            self.build_heap(list_,0,end - 1)
        return list_

    def build_heap(self,list_,start,end):
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child + 1 < end and list_[child] < list_[child + 1]:
                child += 1
            if list_[root] < list_[child]:
                list_[root],list_[child] = list_[child],list_[root]
                root = child
            else:
                break


if __name__ == '__main__':
    list_ = [4,5,1,6,2,7,3,8]
    s = Solution()
    print(s.GetLeastNumbers_Solution(list_,4))























