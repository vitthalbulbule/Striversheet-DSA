nums=[1,0,2,2,2,1,0]

n = len(nums)


count0=0
count1=0
count2=0
for i in range(n):
    if nums[i]==0:
        count0+=1
    elif nums[i]==1:
        count1+=1
    else:
        count2+=1

for i in range(n):
    if count0!=0:
        nums[i]=0
        count0-=1
    elif count1!=0:
        nums[i]=1
        count1-=1
    else:
        nums[i]=2

print(nums)

