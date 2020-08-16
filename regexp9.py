# number of matches to a single character. {5,7} means anything that has between 5 and 7 numbers
# which is why 4567 is not matched

import re

sentence = "12345"

print("Total digit Matches:", len(re.findall("\d", sentence)))

print("The number 5 Matches:", len(re.findall("\d{5}", sentence)))

num = "123 1234 12345 123456 1234567 4567"

print("num matches:", len(re.findall("\d{5,7}", num)))