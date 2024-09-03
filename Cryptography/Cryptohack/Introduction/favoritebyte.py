from pwn import xor

# For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.
# I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.
# 73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d

key = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for i in range(256):
    flag = xor(key, bytes([i]))
    if b'ctf' in flag:
        print(f"flag: {flag.decode()}")
        break