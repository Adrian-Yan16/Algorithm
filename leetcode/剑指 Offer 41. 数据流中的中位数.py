import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半

    # 二分查找
    # 时间：O(n + logn) ，二分查找 logn，插入操作 n
    def addNum(self, num: int) -> None:
        if not self.data:
            self.data.append(num)
            return
        if self.data[0] > num:
            self.data.insert(0,num)
            return
        if self.data[-1] < num:
            self.data.append(num)
            return
        # 二分法插入
        l = 0
        r = len(self.data)
        while l < r - 1:
            mid = (l + r) // 2
            if self.data[mid] < num:
                l = mid
            elif self.data[mid] > num:
                r = mid
            else:
                self.data.insert(mid,num)
                return
        self.data.insert(l + 1,num)

    def findMedian(self) -> float:
        # 时间是O（1）
        l = len(self.data)
        mid = l // 2
        if l % 2 != 0:
            return self.data[mid]
        else:
            return (self.data[mid - 1] + self.data[mid]) / 2.0

    # 大小顶堆
    # 时间：O(logn)
    def addNum2(self, num):
        # 当 m !=n（即 N 为 奇数）：需向 B 添加一个元素。实现方法：将新元素 num 插入至 A ，再将 A 堆顶元素插入至 B ；
        if len(self.A) != len(self.B):
            heapq.heappush(self.A,num)
            numb = -heapq.heappop(self.A)
            heapq.heappush(self.B,numb)
        else:
            # 当 m = n（即 N 为 偶数）：需向 A 添加一个元素。实现方法：将新元素 num插入至 B，再将 B 堆顶元素插入至 A；
            heapq.heappush(self.B, -num)
            numb = -heapq.heappop(self.B)
            heapq.heappush(self.A, numb)

    def findMedian2(self):
        # 如果 m != n,中位数为A的堆顶元素
        if len(self.A) != len(self.B):
            return self.A[0]
        # 如果 m = n，中位数为A和B堆顶元素和的一半
        return (self.A[0] - self.B[0]) / 2.0


if __name__ == '__main__':
    s = MedianFinder()
    s.addNum2(1)
    s.addNum2(2)
    # print(s.findMedian2())
    s.addNum2(3)
    # print(s.findMedian2())