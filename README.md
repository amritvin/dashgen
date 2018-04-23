#dashgen

dashgen is a simple python tool to find Md5,Sha1,Sha2,Sha3 hashes of all files in current directory.


Usage:
	go to the directory you want to scan and find the hashes, and then just call the program!
	
		eg: dashgen {for this run install : "sh install.sh"}
        or python dashgen.py 
		

Output of dashgen is a json string, that follows 

	{ <filename1>: {
			<md5sum>:"md5 hash",
		        <sha1>	:"sha1 hash",
		        <sha2>	:"sha2 hash",
		        <sha3>	:"sha3 hash"
			<size>	:"size of (file)"
		        }} 
		        
