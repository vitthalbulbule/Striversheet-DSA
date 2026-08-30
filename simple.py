# Input: nums = [0, 0, 3, 3, 5, 6]
#
# Output: 4
#
# Explanation:
#
# Resulting array = [0, 3, 5, 6, _, _]
#
# There are 4 distinct elements in nums and the elements marked as _ can have any value.
#

nums = [0,0,3,3,4,4]
# res=[]
# for i in range(len(nums)-1):
#     if nums[i]==nums[i+1]:
#         res.append(nums[i])
#
# print(len(res))
j=0
n=len(nums)
for i in range(1,n):
    if nums[i]!=nums[j]:
        j+=1
        nums[j]=nums[i]
print(nums)
