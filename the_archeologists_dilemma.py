import sys
import math


lines = sys.stdin.readlines()
lines = list(map(lambda x: x.strip(), lines))

for line in lines:
    # length of missing half
    length = len(line)+1
    # begin of the number
    a = int(line)
    # lower and upper limit
    left, right = 1, 0
    while int(right) <= int(left):
        left = math.log(a, 2) + length * math.log(10, 2)
        right = math.log(a + 1, 2) + length * math.log(10, 2)
        length += 1
    print(math.ceil(left))