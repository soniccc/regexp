#Example : replace a string. Not quite what we expected

import re

sentence = "Tart, start, apart, cart, dart"

pattern = re.compile("[ap]art")

sentence = pattern.sub("Spurs", sentence)

print(sentence)
