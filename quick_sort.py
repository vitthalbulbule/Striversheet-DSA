class Solution:
    def partition(self, nums, low, high):
        pivot = nums[low]
        i = low
        j = high

        while i < j:
            while i <= high - 1 and nums[i] < pivot:
                i += 1

            while j >= low + 1 and nums[j] > pivot:
                j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        nums[low], nums[j] = nums[j], nums[low]

        return j

    def quick_sort(self, nums, low, high):
        if low < high:
            p_index = self.partition(nums, low, high)

            self.quick_sort(nums, low, p_index - 1)
            self.quick_sort(nums, p_index + 1, high)

        return nums


obj = Solution()

print(obj.quick_sort(
    [2, 1, 4, 6, 2, 9, 7, 8],
    0,
    7
))