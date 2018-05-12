#!/usr/bin/env python
import subprocess
import os
import json
import sys
import pprint
import timeit
import time
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


start = timeit.default_timer()
for _, dirnames, filenames in os.walk('.'):
    break
arr=filenames
cmd = ["md5sum ","sha1sum ","sha256sum ","sha512sum "] 
result={}
count=0
tot=len(arr)
for files in arr:
	hash={}
 	if files[0]==".":
 		tot=tot-1
 		continue
 	count=count+1
 	if "-q" not in (str(sys.argv)):
 		progress(count,tot,"processing")
	for c in cmd:
		cc=c+files
		proc = subprocess.Popen(cc.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = proc.communicate()
		#print out.split(" ")[0]+" -"+c +" --"+files
		outof= out.split(" ")[0]
		hash[c]=outof
	hash["size"]=os.stat(files).st_size 
	result[files]=hash
stop = timeit.default_timer()
if "-q" not in (str(sys.argv)):
	os.system('clear')
#print json.dumps(result)
pprint.pprint(result)
if "-vq" not in (str(sys.argv)):
	print "\n\t\t\tDone!  ?(`_`)?  Hashes of "+str(count)+" files calculated in "+ str(stop-start)+" secs\n"
