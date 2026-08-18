class Solution:
    def search(self, nums, target):
        n=len(nums)
        for i in range (n):

            if nums[i]==target:
                return i
        return -1
obj = Solution()
nums = [12,1,1,532,21,1]
target = 5327
print(obj.search(nums,target))

