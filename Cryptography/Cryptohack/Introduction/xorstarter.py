from pwn import xor

txt = "label"

print(xor(txt.encode(), 13).decode('utf-8'))