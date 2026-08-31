def missing():
    nums = [0,1,2,4,5,6]

    n=len(nums)
#
#     for i in range(n):
#         if i not in nums:
#             return i
#
#     return n+1
#

# Better Solution
#     sum=0
#     for i in range(n):
#         sum = sum+i

    sum1=0
    for num in nums:
        sum1=sum1+num


    return int((n*(n+1)/2) - sum1)

print(missing())
