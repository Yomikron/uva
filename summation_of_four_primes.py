import sys
import bisect


lines = sys.stdin.readlines()
lines = list(map(lambda x: int(x.strip()), lines))

# sieve
limit = 10000000 + 1
primes = list(range(limit))
primes[1] = 0
# until the square root of limit
for i in range(2, 3163):
    if primes[i]:
        primes[i * i: limit: i] = [0] * len(range(i * i, limit, i))
primes = list(filter(lambda x: x != 0, primes))

for line in lines:
    if line < 8:
        print("Impossible.")
    else:
        result = ""
        if line % 2 == 0:
            # even numbers can be expressed as two primes and 2 plus 2
            result += "2 2 "
            line -= 4
        else:
            # odd numbers can be expressed as two primes and 2 plus 3
            result += "2 3 "
            line -= 5
        # Goldbach's conjecture
        low = 0
        # binary search for high index less or equal the number
        high = bisect.bisect(primes, line) - 1
        while low <= high:
            tmp = primes[low] + primes[high]
            if tmp > line:
                high -= 1
            elif tmp < line:
                low += 1
            else:
                result += str(primes[low]) + " " + str(primes[high])
                break
        print(result)