num =7
count=0
for i in range (1,num):
    if num%i==0:
        count+=1

if count>2:
    print('Not')
else:
    print('true')