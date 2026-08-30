class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        left = self.mergeSort(left)
        right = self.mergeSort(right)
        return self.sort(left, right)

    def sort(self, left, right):
        m = len(left)


        n = len(right)
        result = []
        i = 0
        j = 0
        while i < m and j < n:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        if i < m:
            while i < m:
                result.append(left[i])
                i += 1
        if j < n:
            while j < n:
                result.append(right[j])
                j += 1

        return result
obj = Solution()
nums = [4,2,1,4,2,5,6]
print(obj.mergeSort(nums))