#Example: Match for a range of characters at the start of a word

import re

sentence = "Tart, start, apart, cart, dart, fart"
all_examples = re.findall("[c-f]art", sentence)

print("Example: Match for a range of characters at the start of a word")
for i in all_examples:
    print(i)

#Example: Match for a range of characters NOT at the start of a word

sentence = "Tart, start, apart, cart, dart, fart"
all_examples = re.findall("[^c-f]art", sentence)

print("Example: Match for a range of characters NOT at the start of a word")
for i in all_examples:

    print(i)