import sys


numberOfCases = int(sys.stdin.readline())
# fragments contains each line after the first one as an element
fragments = sys.stdin.readlines()[1:]

# cases is a list of lists of fragments without linebreaks
cases = []
case = []
for f in fragments:
    if f == '\n':
        cases.append(case)
        case = []
    else:
        case.append(f.strip())
cases.append(case)

# lengthsOfFragments is a list containing the lengths of each case
lengthsOfFragments = [int((sum(len(f) for f in c) / (len(c) / 2))) for c in cases]

# contains all possible combinations for each repaired case
repairedCases = []

for c in range(len(cases)):
    combinations = []
    for i in range(len(cases[c])):
        # contains all fragments who could fit together with the one from index i
        fragments = cases[c][:i]+cases[c][i+1:]
        fragments = list(filter(lambda x: len(x) == (lengthsOfFragments[c]-len(cases[c][i])), fragments))
        # set of all combinations possible with the other fragments
        combination_right = set(map(lambda x: cases[c][i] + x, fragments))
        combination_left = set(map(lambda x: x + cases[c][i], fragments))
        combination_right = combination_right.union(combination_left)
        combinations.append(combination_right)
    repairedCases.append(list(combinations[0].intersection(*combinations[1:])))

for i in range(len(repairedCases)):
    for j in repairedCases[i]:
        print(j, sep=' ')
    if i < len(repairedCases)-1:
        print('')