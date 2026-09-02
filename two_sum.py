def twosum():
    nums = [1,3,5,-7,6,-3]
    target = 2

    n=len(nums)
    for i in range(1,n):
        for j in range(n):

            if nums[i]+nums[j]==target:

                return [i,j]
print(twosum())