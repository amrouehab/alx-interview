#!/usr/bin/python3
"""
Prime Game Module
Maria and Ben play a game where they take turns picking prime numbers
and removing them and their multiples from a set of consecutive integers.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game.
    
    Args:
        x: number of rounds
        nums: array of n values for each round
    
    Returns:
        Name of the player that won the most rounds, or None if tie
    """
    if not nums or x <= 0:
        return None
    
    # Find the maximum n to optimize sieve calculation
    max_n = max(nums)
    
    # Sieve of Eratosthenes to find all primes up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    
    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)
    
    maria_wins = 0
    ben_wins = 0
    
    # For each round, determine the winner
    for n in nums:
        # The number of moves in the game equals the number of primes <= n
        moves = prime_count[n]
        
        # If odd number of moves, Maria wins (she goes first)
        # If even number of moves, Ben wins
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
