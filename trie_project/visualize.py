#imports
import json
from trie import file_text

# function to return a new dict template
def struct():
    struct = {
        'iw': 'False'
    }
    return struct

# getting list of words as input
file_len = len(file_text)


# trie making stuff happening (hard to explain)
tmp_s = struct()
root = tmp_s
for c in file_text:
    if c != '\n':
        if c not in tmp_s:
            tmp_s[c] = struct()
        tmp_s = tmp_s[c]
    elif c == '\n':
        tmp_s['iw'] = 'True'
        tmp_s = root
        cur_word = []

# saving the trie in a json file
with open('output.json', 'w') as fp:
    json.dump(root, fp, indent=4)
