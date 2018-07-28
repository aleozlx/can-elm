with open('sample') as f:
	for line in f.readlines():
		print(line[:24].strip())