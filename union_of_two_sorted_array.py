# num1=[1,2,3,4,5]
# num2=[1,2,7]

num1 = [3, 4, 6, 7, 9, 9]
num2 = [1, 5, 7, 8, 8]

n1=len(num1)
n2=len(num2)
res=[]

i=0
j=0
while i<n1 and j<n2:

    if num1[i]==num2[j]:
        res.append(num1[i])
        i+=1
        j+=1
    elif num1[i]!=num2[j] and num1[i]<num2[j]:
        if res[-1]!=num1[j]:
            res.append(num1[i])
            i+=1
    else:
        res.append(num2[j])
        j+=1

print(res)
