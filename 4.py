#! /usr/local/bin/python
# Solution: www.pythonchallenge.com/pcc/def/peak.html

import urllib
import re

initial_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"

url = initial_url
counter = 0
while counter <= 400:
    response = urllib.urlopen(url)
    counter += 1
    prev_number = re.findall(r'\d+', url)[0]
    html = response.read()
    print html
    try:
        new_number = re.findall(r'\d+', html)[-1]
        if new_number:
	    url = url.replace(prev_number, new_number)
    except:
        import pdb; pdb.set_trace()
