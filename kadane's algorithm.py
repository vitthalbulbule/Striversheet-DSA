nums = [2,3,5,-2,7,-4]
maximum = float('-inf')

n=len(nums)
total = 0

best_start = 0
start = 0
end = 0

for i in range(n):
    total+=nums[i]

    if total>maximum:
        maximum=total
        best_start = start
        end = i

    if total<0:

        total = 0
        start = i+1

subarray = nums[best_start:end+1]

print(subarray)
print(maximum)

