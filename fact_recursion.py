
#
# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(5))

# Input: s = " -12345"
#
# Output: -12345
#
# Explanation:
#
# Ignore leading whitespaces.
# The sign '-' is encountered, indicating the number is negative.
# Digits 12345 are read and converted to -12345.

# def atoi(n,i=0,num=0,sign=1):
#
#     sign = 1
#
#
#
#
#     if i<len(n) and n[i]==' ':
#         return atoi(n,i+1,num)
#
#     if i < len(n) and n[i] == '-':
#         sign = -1
#         i += 1
#
#     if i>len(n) or not n[i].isdigit():
#         return num
#
#     num = num *10 + int(n[i])
#
#     num = num*sign
#
#     return atoi(n,i+1,num)
#
# print(atoi('-123He'))


def atoi(s, i=0, num=0, sign=1):

    # 1. Ignore leading spaces
    if i < len(s) and s[i] == ' ':
        return atoi(s, i + 1, num, sign)

    # 2. Check sign
    if i < len(s) and s[i] == '-':
        sign = -1
        i += 1

    elif i < len(s) and s[i] == '+':
        sign = 1
        i += 1

    # 3. Stop at non-digit
    if i >= len(s) or not s[i].isdigit():
        return sign * num

    # 4. Build number
    num = num * 10 + int(s[i])

    # 5. Recursive call
    return atoi(s, i + 1, num, sign)


print(atoi(" -1235"))