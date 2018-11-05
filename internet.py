#!/usr/local/bin/python

import subprocess, time

hosts = ('8.8.8.8', 'kernel.org', 'yahoo.com')

def ping(host):
  ret = subprocess.call(['ping', '-c', '1', '-W', '5', host],
    stdout=open('/dev/null', 'w'),
    stderr=open('/dev/null', 'w'))
  return ret == 0  #return 1 in not connection case

def main():
  status = False

  for h in hosts:
    if(~status):
      if ping(h):
        status = True
      
  if status:
       print("internet available")
  else:
       print("internet not available")  

main()