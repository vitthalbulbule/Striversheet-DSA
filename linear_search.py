def find():
    nums = [1,2,3,4,5]
    target=40

    n=len(nums)

    for i in range(n):
        if nums[i]==target:
            return i
    return -1

print(find())