class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        best_profit=0
        for i in range(len(prices)):
            todayprofit=prices[i]-min_price 
            if prices[i] < min_price :
               min_price=prices[i]
            elif todayprofit > best_profit :
                best_profit=todayprofit
        return best_profit
               
               