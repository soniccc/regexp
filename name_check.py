import re
from regexp_name import name_check

name = input("Please enter you first and last names: ")
pattern = re.compile("\w{2,20}\s\w{2,20}")

name_check(pattern, name)

