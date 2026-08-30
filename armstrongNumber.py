n=151
original = n

count=0
num = n
while num>0:
    count+=1
    num = num //10

num = n
total = 0

while num>0:

    digit = num%10
    total += digit ** count
    num = num//10

if original==total:
    print(True)
else:
    print(False)