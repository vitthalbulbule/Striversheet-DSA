

def setZeros(nums):
    r = len(nums)
    c = len(nums[0])

    for i in range(0,r):
        for j in range(0,c):
            if nums[i][j]==0:
                markInfinity(nums,i,j)
    for i in range(0,r):
        for j in range(0,c):
            if nums[i][j]==float('inf'):
                nums[i][j]=0
    return nums

def markInfinity(nums,row,col):
    r = len(nums)
    c = len(nums[0])

    for i in range(0,r):
        if nums[i][col] !=0:
            nums[i][col]=float('inf')

    for j in range(0,c):
        if nums[row][j]!=0:
            nums[row][j]=float('inf')

nums = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeros(nums))





