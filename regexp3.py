#Example: to locate the word 'spur' in the sentence. The location is the
# index values of the word, start and stop.

import re

sentence = "spurs is the nickname for Tottenham Hotspur Football Club"

iter_object = re.finditer("spur", sentence)

for i in iter_object:

    location_tuple = i.span()

    print(location_tuple)
    # prints the word at these locations. Which we already stipulated but just 
    # included as an example for group method for the iterable object
    print(i.group(0))