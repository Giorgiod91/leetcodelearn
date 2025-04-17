from typing import List

def maxProfit(prices: List[int]) -> int:
    # Initialize variables
    min_price = float('inf')  # Initially set to infinity
    max_profit = 0  # Start with no profit

    # Iterate through the prices list
    for price in prices:
        # If the current price is lower than the min_price, update min_price
        if price < min_price:
            min_price = price
        # Calculate profit if we sell on the current day
        profit = price - min_price
        # Update max_profit if the current profit is greater
        if profit > max_profit:
            max_profit = profit

    return max_profit




