class solution:
  def buyAndSellStock(self,prices):

    min_price = prices[0]
    max_profit = 0

    for i in prices:
      profit = i - min_price
      max_profit = max(max_profit,profit)
      min_price = min(min_price,i)

    return max_profit

prices = [7,1,5,3,6,4]
s = solution()
result = s.buyAndSellStock(prices)
print(result)