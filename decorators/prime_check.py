def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_gen():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

prime_num = prime_gen()

for l in range(20):
    print(next(prime_num))




