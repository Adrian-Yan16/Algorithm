import heapq

class Solution:
    def getLeastNumbers(self, arr, k: int):
        arr.sort()
        return arr[:k]

    def getLeastNumbers2(self, arr, k: int):
        temp = []
        res = []
        for i in arr:
            heapq.heappush(temp,i)
        for j in range(k):
            res.append(heapq.heappop(temp))
        return res

    # 堆
    def getLeastNumbers3(self, arr, k: int):
        if not k or not arr:
            return []
        if k > len(arr):
            return arr
        heap = arr[:k]
        first = k // 2 - 1
        for i in range(first,-1,-1):
            self.build_heap(heap,i,k-1)
        for i in range(k,len(arr)):
            if arr[i] < heap[0]:
                heap[0] = arr[i]
                self.build_heap(heap,0,k-1)
        return heap

    def build_heap(self,list_,root,end):
        while True:
            child = root * 2 + 1
            if child > len(list_):
                return
            if child + 1 <= end and list_[child + 1] > list_[child]:
                child += 1
            if child <= end and list_[root] < list_[child]:
                list_[root],list_[child] = list_[child],list_[root]
                root = child
            else:
                break

    # 快排
    def getLeastNumbers4(self, arr, k: int):
        if k >= len(arr):
            return arr
        def quick_sort(l,r):
            i = l
            j = r
            while i < j:
                # 自左向右，找到第一个大于哨兵的数
                while i < j and arr[i] <= arr[l]:
                    i += 1
                # 自右向左，找到第一个小于哨兵的数
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                arr[i],arr[j] = arr[j],arr[i]
            # i=j时，退出循环，并与哨兵交换位置
            # 则大于哨兵的在右边，小的在左边
            arr[i],arr[l] = arr[l],arr[i]
            if k < i:
                return quick_sort(l,i - 1)
            if k > i:
                return quick_sort(i+1,r)
            return arr[:k]
        return quick_sort(0,len(arr))



if __name__ == '__main__':
    s = Solution()
    print(s.getLeastNumbers([4,5,1,6,2,7,3,8],4))
    print(s.getLeastNumbers2([4,5,1,6,2,7,3,8],4))
    print(s.getLeastNumbers3([0,0,0,2,0,5],0))
