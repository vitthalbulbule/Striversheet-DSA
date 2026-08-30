class Solution:
    def search(self, nums, target):
        n=len(nums)
        # for i in range (n):
        #
        #     if nums[i]==target:
        #         return i
        # return -1
        i=0
        j=n-1
        mid = len(nums)//2
        while i<=j:
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j=j-1
            else:
                i=i+1
        return -1

obj = Solution()
nums = [12,1,1,532,21,1]
target = 532
print(obj.search(nums,target))

