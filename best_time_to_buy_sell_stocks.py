def maxProfit(prices):
    """
    Calculates the maximum profit that can be achieved by buying and selling a stock once.

    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a
    different day in the future to sell that stock.

    Args:
        prices: A list of integers representing the price of the stock on each day.

    Returns:
        The maximum profit that can be achieved. If no profit can be made, returns 0.
    """
    min_price = float('inf')
    max_profit = 0

    # Iterate through the prices to find the best buy and sell days
    for price in prices:
        # If the current price is lower than the minimum price found so far,
        # update the minimum price. This is our potential buy day.
        if price < min_price:
            min_price = price
        # Otherwise, calculate the potential profit if we were to sell on the current day.
        # If this profit is greater than our max profit so far, update the max profit.
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Example 1:
prices1 = [7, 1, 5, 3, 6, 4]
print(f"For prices {prices1}, the maximum profit is: {maxProfit(prices1)}")

# Example 2:
prices2 = [7, 6, 4, 3, 1]
print(f"For prices {prices2}, the maximum profit is: {maxProfit(prices2)}")

# Custom Example:
prices3 = [2, 4, 1]
print(f"For prices {prices3}, the maximum profit is: {maxProfit(prices3)}")
