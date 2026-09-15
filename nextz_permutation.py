nums = [1,2,3]
n=len(nums)
for j in range(n-2,-1,-1):
    if nums[j]<nums[j+1]:
        pivot=nums[j]

nums[j],nums[j+1]=nums[j+1],nums[j]



print(pivot)
print(nums)

