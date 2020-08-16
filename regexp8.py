#Example: Substitue new line with a space. Experiment with this script using
# \b \f \r \t \v instead of a space

import re

sentence = '''
We are Tottenhan,
Super Tottenham,
from the Lane.
'''

pattern = re.compile("\n")

sentence = pattern.sub(" ", sentence)

print(sentence)