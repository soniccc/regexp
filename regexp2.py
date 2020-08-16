# Example: To verify a string contans a particular word

import re

paragraph = '''
The regular expression isolates the document's namespace value, which is then used to compose findable values for tag names
'''

word = 'namespace'

if re.search(word, paragraph):
    print(f"The paragraph contains the word : '{word}'")
else:
    print(f"The word '{word}' is not in this paragraph")


