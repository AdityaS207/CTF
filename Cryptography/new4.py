import base64

ord = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byte_data = bytes.fromhex(ord)
raw = base64.b64encode(byte_data)
flag = raw.decode('utf-8')
print(flag)