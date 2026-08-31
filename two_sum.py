def twosum():
    nums = [1,3,5,-7,6,-3]
    target = 2
    res = []
    n=len(nums)
    for i in range(1,n):
        for j in range(n):

            if nums[i]+nums[j]==target:
                res.append(i)
                res.append(j)
                return res
print(twosum())