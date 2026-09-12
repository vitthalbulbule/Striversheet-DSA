# def show():
#     nums =[[1,2],[4,5]]
#
#     n=len(nums)
#     res = [ [ 0 for _ in range(n)] for _ in range(n)]
#
#     for i in range(0,n):
#         x=i
#         for j in range(0,n):
#
#             if i==x:
#                 nums[i][j]=nums[j][[n-1]-i]
#                 x+=1
#     return nums
# print(show())


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n=len(matrix)

for i in range(0,n-1):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]


for i in range(n):
    matrix[i].reverse()

print(matrix)