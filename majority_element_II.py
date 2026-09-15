# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         size = n/3
#         dict = {}
#
#         for num in nums:
#             dict[num] = 0
#
#         for num in nums:
#             dict[num] += 1
#
#         for k, v in dict.items():
#             if v > size:
#                 return k
#
#
# obj=Solution()
# print(obj.majorityElement(nums=[3,2,3]))

nums=[1]
# nums.sort()
n=len(nums)
size = n/3
# res=[]
# count=1
# for i in range(n-1):
#     if nums[i]==nums[i+1]:
#         count+=1
#
#         if count>size:
#             res.append(nums[i])
#     else:
#         count=1
# print(res)



# Boyer Moore Algorithm
freq=0
for i in range(n):
    if freq==0:
        ans=nums[i]
    if ans==nums[i]:
        freq+=1
    else:
        freq-=1
print(ans)