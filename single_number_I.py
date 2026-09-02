# nums = [4,1,2,1,2]
nums = [1, 2, 2, 4, 3, 1, 4]
n=len(nums)
dict={}



for num in nums:

    dict[num]=0
# for num in nums:
#     if num in dict:
#         dict[num]+=1
#     else:
#         dict[num]=1





print(dict)

# class Solution(object):
#     def singleNumber(self, nums):
#
#         n = len(nums)
#         freq_map = {}
#         # for i in range(n):
#         #     freq_map[i] = 0
#
#         for num in nums:
#
#             freq_map[num] = 0
#
#         for k, v in freq_map.items():
#             if v == 1:
#                 return k
# nums = [4]
# obj = Solution()
# print(obj.singleNumber(nums))