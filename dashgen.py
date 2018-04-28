#!/usr/bin/env python
import subprocess
import os
import json
import sys
import pprint
import timeit

start = timeit.default_timer()
for _, dirnames, filenames in os.walk('.'):
    break
arr=filenames
cmd = ["md5sum ","sha1sum ","sha256sum ","sha512sum "] 
result={}
count=0
for files in arr:
	hash={}
 	if files[0]==".":
 		continue
 	count=count+1
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
#print json.dumps(result)
pprint.pprint(result)
print "\n\t\t\tDone!  ?(`_`)?  Hashes of "+str(count)+" files calculated in "+ str(stop-start)+" secs\n"

