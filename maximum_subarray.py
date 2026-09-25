nums=[2,3,-1,2,4]

prefix=1
suffix=1
ans=float('-inf')
n=len(nums)
# for i in range(n):
#     if prefix==0:
#         prefix=1
#     if suffix==0:
#         suffix=1
#
#
#     prefix*=nums[i]
#     suffix*=nums[n-1-i]
#     ans = max(ans,prefix,suffix)
#
# print(ans)

n=len(nums)
total=1
ans=float('-inf')

for i in range(n):

    total=total*nums[i]
    ans = max(ans,total)

    if total<0:
        total = 1
print(ans)
