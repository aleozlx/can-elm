import time

time.sleep(5)

# print("ATL0")
# print("ATAL")
# print("ATPBC001")
# print("ATH1")

# while 1:
# 	print("ATMA")

import serial, re
with serial.Serial('/dev/rfcomm0', 9600, parity='N', bytesize=8, stopbits=1, timeout=1) as ser:
	for i in range(3):
		ser.write(b'ATDP\r')
		ser.write(b'ATE0\r')
	# ser.write(b'ATL1\r')
		print(ser.readline())
		time.sleep(1)
	
	a = set()
	rule = re.compile(r'^([0-9A-F]{2} ){8}')
	while 1:
		try:
			ser.write(b'ATMA\r')
			res = str(ser.readline().decode('ascii'))
			if rule.match(res):
				print(res.strip())
		except UnicodeDecodeError:
			pass
		# a.add(res)
		# # print(len(a))
		# print(res)



