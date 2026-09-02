# class Solution:
#     def bubbleSort(self, nums, n):
#         if n == 1:
#             return
#
#         for i in range(n - 1):
#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#
#         return self.bubbleSort(nums, n - 1)
#
#
# obj=Solution()
# nums=[3,1,7,4,5,1,9,11]
# print(obj.bubbleSort(nums,n=8))
class Solution:
    def bubbleSort(self, nums, n):
        if n == 1:
            return nums

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return self.bubbleSort(nums, n - 1)


obj = Solution()
nums = [1,0,2,1,0]

print(obj.bubbleSort(nums, len(nums)))