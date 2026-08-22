
def sort(nums,digitt):
    res=[]
    count=0
    for i in range(len(nums)):
        while nums[i]>0:
            digit = nums[i]%10

            nums[i]=nums[i]//10

            if digit == digitt:
                count+=1
    print(count)
sort(nums=[12,54,32,22] , digitt=2)