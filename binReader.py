import sys
import binascii

#Import from stdin:
data = sys.stdin.buffer.read()


#Load to bytearray:
#barr = bytearray(data.read())
barr = bytearray(data)

#Do modification:
for i in range(len(barr)):
  barr[i]+=1

#output bytearray to stdout
sys.stdout.write(barr.hex())
