# Validate email addresses

import re

email = "bob@gmail.com sk@.hotmail.com @ba.com jeff@.co.uk"

print("EmailMatches:", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email)))

