from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.size = 0
        self.nums = SortedList()

    def addNum(self, num: int) -> None:
        self.nums.add(num)
        self.size += 1
        
    def findMedian(self) -> float:
        if self.size % 2 == 1:
            index = (self.size // 2) 
            return self.nums[index]
        else:
            mid = self.size // 2
            return (self.nums[mid - 1] + self.nums[mid]) / 2
            

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()