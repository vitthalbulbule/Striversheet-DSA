# Brute Forst Solution

# def fun():
#     nums = [1,2,5,3,1,2]
#
#     n=len(nums)
#     res=[]
#
#     for i in range(n):
#         flag = True
#         for j in range(i+1,n):
#
#             if nums[i]<nums[j]:
#                 flag=False
#                 break
#
#         if flag:
#
#             res.append(nums[i])
#     return res
# print(fun())


# Optimal Solution
class Solution:
    def leaders(self, nums):
        n = len(nums)

        res = []
        max_right = float('-inf')

        for i in range(n - 1, -1, -1):
            if nums[i] >= max_right:
                res.append(nums[i])
                max_right = nums[i]

        res.reverse()
        return res
nums= [1,2,5,3,1,2]
obj = Solution()
print(obj.leaders(nums))
