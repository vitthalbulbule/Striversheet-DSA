class Solution:

    def reverse(se, nums, left, right):
        n = len(nums)

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums, k):
        n = len(nums)

        k = k % n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        print(nums)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

obj = Solution()
obj.rotate(nums, k)

print(nums)


