from regexp_phone import check
import re

pattern = re.compile("\d{4}-\d{3}-\d{4}")

number = input("Please enter your telephone number: ")

check(number, pattern)

