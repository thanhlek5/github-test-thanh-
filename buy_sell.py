# ĐÃ HOÀN THÀNH ++++
# def maxProfit(price):
#     l = 1
#     n =0
#     maxP = 0
#     while n < len(price):
#         if price[n]<price[l]:
#             profit = price[l]-price[n]
#             maxP = max(maxP,profit)  # max(maxP,profit) so sánh hai giá trị maxP và profit và gán giá trị lớn nhất cho maxP
#         else:
#             l = l +1
#         n += 1
#     return maxP
# list = [7,1,5,3,6,4]
# print(maxProfit(list))

# def maxProfit(price):
#     maxP = 0
#     n = 0  # ngày mua
#     l = 1   # ngày bán
#     while n < len(price):
#         while l < len(price[n+1:]):
#             if price[n]<price[l]:
#                 Profit = price[l]-price[n]
#                 maxP = max(maxP,Profit)
#             else:
#                 l +=1
#         n +=1
#     return maxP
# list = [7,1,5,3,6,4]
# print(maxProfit(list))

def maxProfit(price):
    maxP = 0
    for n in range(len(price)):
        for l in range(n+1, len(price)):
            if price[n] < price[l]:
                Profit = price[l] - price[n]
                maxP = max(maxP, Profit)
    return maxP

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))

