# Validate phone numbers

# \w is equivalent to [a-zA-Z0-9]
# \W is equivalent to [^a-zA-Z0-9]
import re

phone_number = "0208-577-6236"

pattern = re.compile("\w{4}-\w{3}-\w{4}")

def check(phone_number, pattern):
    if re.search(pattern, phone_number):
        print("This is a valid phone number")
        return "This is a valid phone number"
    else:
        print("This is NOT a valid phone number")
        return "This is a NOT valid phone number"

if __name__ == "__main__":
    check(phone_number, pattern)