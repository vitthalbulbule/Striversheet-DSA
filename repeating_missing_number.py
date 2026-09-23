class Solution:
    def findMissingRepeatingNumbers(self, nums):

        n = len(nums)
        freq = [0] * (n + 1)

        for num in nums:
            freq[num] += 1

        print(freq)

        repeating = -1
        missing = -1

        for num in range(1, n + 1):

            if freq[num] == 2:
                repeating = num

            elif freq[num] == 0:
                missing = num

            if repeating != -1 and missing != 1:
                break

        return [repeating, missing]




ob = Solution()
print(ob.findMissingRepeatingNumbers(nums=[[9,1,7],[8,9,2],[3,4,6]]))
