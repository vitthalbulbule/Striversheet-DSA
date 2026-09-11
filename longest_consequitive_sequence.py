nums=[1,2,5,6,3,2,100,34,1]
n=len(nums)
my_set = set()
longest = float('-inf')

for i in range(n):
    my_set.add(nums[i])

for num in my_set:

    if num-1 not in my_set:
        x=num
        count=1

        while x+1 in my_set:
            count+=1
            x+=1
        longest = max(longest,count)
print(longest)
