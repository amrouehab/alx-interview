#!/usr/bin/python3
"""
Module for making change problem
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): List of coin denominations available.
        total (int): The target amount to reach with the coins.
    
    Returns:
        int: Fewest number of coins needed to meet the total. Returns -1 if total cannot be met.
    """
    if total <= 0:
        return 0
    
    # Initialize a DP array where dp[i] will store the min coins for amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for 0 amount
    
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1
    
    return dp[total] if dp[total] != float('inf') else -1
