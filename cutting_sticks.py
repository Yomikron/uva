import sys
import numpy
from operator import add


lines = sys.stdin.readlines()
sticks = []
i = 0
while int(lines[i]):
    stick_length = int(lines[i])
    points = [0] + list(map(int, lines[i+2].split())) + [stick_length]
    sticks.append(points)
    i += 3

for stick in sticks:
    opt = numpy.empty((len(stick), len(stick),))
    opt[:] = numpy.nan
    for i in range(len(stick)-1):
        # base case
        opt[i, i+1] = 0
    for part in range(2, len(stick)):
        for i in range(len(stick)-part):
            j = i + part
            # we have to pay anyway the cut between i and j
            segment = stick[j] - stick[i]
            # minimum of costs when doing all cuts between i and j
            costs = list(map(add, opt[i, i+1:j], opt[i+1:j, j]))
            min_cost = min(costs)
            # minimal cost of cutting the stick from i to j
            opt[i, j] = segment + min_cost
    print('The minimum cutting is {}.'.format(int(opt[0, len(stick)-1])))
