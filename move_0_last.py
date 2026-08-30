# nums=[0, 1,4,0,5,2]
# n = len(nums)
#
# i=0
# j=1
#
# while j<=n-1:
#     if nums[i]==0 and nums[j]!=0:
#         nums[i],nums[j]=nums[j],nums[i]
#         i+=1
#         j+=1
#     else:
#         j+=1
# print(nums)

class Solution:
    def moveZeroes(self,nums):
        nums=[0, 1,4,0,5,2]
        n = len(nums)

        i=0
        j=1

        while j<=n-1:
            if nums[i]==0 and nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            else:
                j+=1
        print(nums)

s =Solution()
print(s.moveZeroes(nums=[0,1,4,5,2]))