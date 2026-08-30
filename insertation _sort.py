def insertation_sort(nums):



    n=len(nums)

    for i in range(1,n):
        key = nums[i]
        j=i-1

        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key

    return nums
nums = [3,4,2,1,10,6,2,111,23]
print(insertation_sort(nums))

