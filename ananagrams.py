# list of all words
words = []
# read input line
while True:
    line = input()
    if line is not '#':
        words += line.split()
    else:
        break
# dict hashes all words in lower case and alphabetically ordered as keys
words_dict = {}
for w in words:
    w_key = ''.join(sorted(w.lower()))
    # set value to # if key already exists
    if w_key in words_dict:
        words_dict[w_key] = '#'
    # store word if key does not exit yet
    else:
        words_dict[w_key] = w
# filter all words which key has been hashed only once
ananagrams_list = list(filter(lambda v: v is not '#', words_dict.values()))
ananagrams_list.sort()
# print each ananagram
for a in ananagrams_list:
    print(a, end="\n")