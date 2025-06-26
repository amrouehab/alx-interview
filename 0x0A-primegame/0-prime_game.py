#!/usr/bin/python3

def sieve(n):
    """Returns a list of the number of primes up to index i for i in range(n + 1)."""
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count
    return prime_count

def isWinner(x, nums):
    """Determines the winner of the prime game."""
    if not nums or x < 1:
        return None
    max_num = max(nums)
    prime_counts = sieve(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

