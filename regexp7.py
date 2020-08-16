#Example: searching a string with special characters by converting sentence
# into a raw string

import re

sentence = "The pattern to search for is \\Tottenham"

print(re.search(r"\\Tottenham", sentence))