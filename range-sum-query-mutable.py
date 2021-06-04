class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.memo = {}

    def update(self, index: int, val: int) -> None:
        prev_val = self.nums[index]
        self.nums[index] = val
        for left, right in self.memo:
            if index >= left and index <= right:
                self.memo[(left, right)] += -prev_val + val

    def sumRange(self, left: int, right: int) -> int:
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        self.memo[(left, right)] = sum(self.nums[left:right + 1])
        return self.memo[(left, right)]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
