#Example : find a substring within words in a sentence. Notice that Tart and start
# are not printed from the for loop

import re

sentence = "Tart, start, apart, cart"

all_examples = re.findall("[tsac]art", sentence)

for i in all_examples:

    print(i)