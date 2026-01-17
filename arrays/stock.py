#buy and sell stock for best profit
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')   # track the lowest price seen so far
        max_profit = 0             # track the best profit

        for price in prices:
            # update the minimum price
            if price < min_price:
                min_price = price

            # calculate profit if we sell today
            profit = price - min_price

            # update the maximum profit
            if profit > max_profit:
                max_profit = profit

        return max_profit

        
