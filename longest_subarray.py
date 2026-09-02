def longest_subarray(nums, k):

    prefix_sum = 0
    max_length = 0

    prefix_map = {0: -1}

    for i in range(len(nums)):

        prefix_sum += nums[i]

        if prefix_sum - k in prefix_map:

            length = i - prefix_map[prefix_sum - k]

            max_length = max(max_length, length)

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_length



print(subarraySum(nums=[1,2,3,1,1,1,1,2,6],k=6))

# nums = [10,5,2,7,1,9]
# k=15
# n = len(nums)
# msx_len = 0
#
# for i in range(n):
#     sum=0
#     for j in range(i,n):
#         sum+=nums[j]
#
#         if sum==k:
#             length = j-i+1
#             msx_len = max(msx_len,length)
# print(msx_len)
