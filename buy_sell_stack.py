# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         n = len(prices)
#         profit = 0
#         for i in range(n-1):
#             differ = 0
#             for j in range(i+1,n):
#
#                 if prices[i]<prices[j]:
#                     differ = prices[j]-prices[i]
#                     profit = max(differ,profit)
#
#         return profit
#
# obj = Solution()
# print(obj.maxProfit(prices=[7,6,4,3,1]))
def cal():
    prices = [7,6,4,3,1]
    n = len(prices)
    profit = 0
    i=0
    j=i+1
    while i<=n-1:

        if prices[i]<prices[j]:
            differ = prices[j]-prices[i]
            profit = max(differ,profit)
            j+=1

        else:
            j+=1



        if j == n-1:
            i+=1
            j=i+1
        if i==n-1:
            return
    print(profit)
print(cal())

