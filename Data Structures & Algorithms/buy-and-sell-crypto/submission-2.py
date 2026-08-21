class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        curr_max_profit = 0
        for i in range(len(prices)):
            j = i + 1
            while j < len(prices):
                profit = prices[j] - prices[i]
                if profit > curr_max_profit:
                    curr_max_profit = profit
                j += 1
        return curr_max_profit
        '''
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit,price-min_price)
            min_price  = min(min_price,price)
        return max_profit