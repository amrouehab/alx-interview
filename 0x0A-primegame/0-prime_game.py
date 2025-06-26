#!/usr/bin/python3

def is_prime(n):
    """Check if number is a prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_count(n):
    """Return number of prime numbers <= n using sieve"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    count = 0
    for i in range(2, n + 1):
        if sieve[i]:
            count += 1
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return count

def isWinner(x, nums):
    """Determine the winner of the prime game"""
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        primes = prime_count(nums[i])
        if primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
