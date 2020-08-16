#Check that the name is separated by a space and appears to be a first and second name
# use the \s

# \s [\f\n\r\t\v]
# \S [^\f\n\r\t\v]

import re

name = "Harry Kane"
pattern = re.compile("\w{2,20}\s\w{2,20}")

def name_check(pattern, name):
    if re.search(pattern, name):
        print("This is a valid name")
        return "This is a valid name"
    else:
        print("This is a NOT valid name")
        return "This is NOT a valid name"



if __name__ == "__main__":
    name_check(pattern, name)