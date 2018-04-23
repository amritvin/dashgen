#!/usr/bin/env python
import subprocess
import os
import json
import sys
arg="."
arr=os.listdir(arg)
cmd = ["md5sum ","sha1sum ","sha256sum ","sha512sum "] 
result={}

for files in arr:
	hash={}
	for c in cmd:
		cc=c+files
		proc = subprocess.Popen(cc.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = proc.communicate()
		#print out.split(" ")[0]+" -"+c +" --"+files
		outof= out.split(" ")[0]
		hash[c]=outof
	hash["size"]=os.stat(files).st_size 
	result[files]=hash
print json.dumps(result)


