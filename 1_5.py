n = 30

is_prime = [True] * (n + 1)

for p in range(2, n + 1):
    if is_prime[p]:
        for i in range(p * 2, n + 1, p):
            is_prime[i] = False

primes = [num for num in range(2, n + 1) if is_prime[num]]
print(primes)
