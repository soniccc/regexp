# Example: To extract the names and ages from a string and place in a python 
# dictionary. Key : Value is Name: Age

import re

Nameage = '''
Lucy is 19 and Jeff is 31
Joe is 36 and Diana is 42
'''

ages = re.findall(r'\d{1,3}', Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)

ageDict = {}

n = 0

for name in names:
    ageDict[name] = ages[n]
    n+=1

print(ageDict)

