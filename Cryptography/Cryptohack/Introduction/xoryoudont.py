from pwn import xor
import binascii

# For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.
# I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.
# 73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d

# txt = ""
txt = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
format_flag = "crypto{"
key = "myXORkey"
# print(xor(txt, format_flag))
print(xor(txt, key))
# for i in range(256):
#     flag = xor(key, bytes([i]))
#     if b'ctf' in flag:
#         print(f"flag: {flag.decode()}")
#         break