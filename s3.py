#!/usr/bin/env python
import requests
import sys

url = 'https://s3.amazonaws.com/'
name = sys.argv[1].strip()

common = ['-test','-dev','-bucket','-s3','_test','_dev','-aws']

url = url + name

def check_code(r, name):
  if r.status_code == 404: print "None",
  elif r.status_code == 403: print "Secure",
  elif r.status_code == 301: print "Redirect",
  elif r.status_code == 200: print "BINGO!",
  elif r.status_code == 400: print "BadName",
  else: print r.status_code,
  print name
  return

def get_code(url, name):
  r = requests.get(url)
  check_code(r, name)
  if r.status_code == 403 or r.status_code == 200:
    for ext in common:
      r = requests.get(url + ext)
      check_code(r, name + ext)
  

get_code(url, name)
if '.' in name:
  n2 = 'www.' + name
  url = 'https://s3.amazonaws.com/' + n2
  get_code(url, n2)
  n3 = name.split('.')[0]
  url = 'https://s3.amazonaws.com/' + n3
  get_code(url, n3)
  



