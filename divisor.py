# n=6
#
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=' ')

n1=9
n2=8
n11=[]
n22=[]

for i in range(1,n1+1):
    if n1%i==0:
        n11.append(i)
print(n11)

for j in range(1,n2+1):
    if n2%j==0:
        n22.append(j)
print(n22)

res=[]
for i in range(len(n11)):
    for j in range(len(n22)):
        if n11[i]==n22[j] and n11[i+1]!=n22[j+1]:
            print(n11[i])


# res=[]
# for i in range(1,n1+1):
#     for j in range(1,n2+1):
#         if n1%i==0 and n2%j==0:
#             res.append(i)
#
# print(res)