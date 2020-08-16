#Example: webscraping phone numbers

import urllib.request
from re import findall
url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"

response = urllib.request.urlopen(url)

html = response.read()

html_string = html.decode()

phone_data = findall("\(\d{3}\) \d{3}-\d{4}", html_string)

for i in phone_data:
    print(i)0