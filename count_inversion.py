def merge(nums):

    if len(nums) <= 1:
        return nums, 0

    mid = len(nums) // 2

    left, count1 = merge(nums[:mid])
    right, count2 = merge(nums[mid:])

    res = []
    n = len(left)
    mid=n-1
    m = len(right)

    i = 0
    j = 0
    count3 = 0

    while i < n and j < m:

        if left[i] <= right[j]:
            res.append(left[i])
            i += 1

        else:
            count3 += (mid-i+1)
            res.append(right[j])
            j += 1

    res += left[i:]
    res += right[j:]

    return res, count1 + count2 + count3


nums = [2, 3, 7, 1, 3, 5]

_, count = merge(nums)

print(count)