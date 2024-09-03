from pwn import xor

# txt ="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
# txt = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
txt = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
for i in range (255):
    print(f"{xor(bytes.fromhex(txt), i)}")

# flag = "crypto"

# # print(bytes.fromhex(txt).decode('utf-8'))
# for i in range(255):
#     # print(xor(bytes.fromhex(txt), i).decode('utf-8'))
#     if flag in xor(bytes.fromhex(txt), i).decode('utf-8'):
#         print(f"{xor(bytes.fromhex(txt), i).decode('utf-8')}")
#         break
