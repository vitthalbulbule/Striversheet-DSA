def second_large(nums):
    n=len(nums)
    large = float('-inf')
    small = float('inf')

    for i in range(n):
        if nums[i]>large:
            small=large
            large = nums[i]
        elif nums[i]>small and nums[i]!=large:
            small = nums[i]
    return small
nums = [7,4,1,5,3]
print(second_large(nums))