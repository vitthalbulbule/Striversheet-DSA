class Solution:
    def isPalindrome(self, n):
        num = n
        rev = 0
        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10
        

        if n==rev:
            return True
        else:
            return False

obj = Solution()
print(obj.isPalindrome(121))