#!/usr/bin/env python
import requests
import sys

url = 'https://s3.amazonaws.com/'
name = sys.argv[1].strip()

url = url + name

r = requests.get(url)
if r.status_code == 404: print "None",
elif r.status_code == 403: print "Secure",
elif r.status_code == 301: print "Redirect",
elif r.status_code == 200: print "BINGO!",
elif r.status_code == 400: print "BadName",
else: print r.status_code,
print name

