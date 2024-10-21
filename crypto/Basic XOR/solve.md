```py
import string

def xor(msg, key):
    o = ''
    for i in range(len(msg)):
        o += chr(ord(msg[i]) ^ ord(key[i % len(key)]))
    return o

with open('encrypted', 'r') as f:
    msg = ''.join(f.readlines())
part_of_msg = 'BUETCTF{'

for i in range(len(msg)):
    candidate = xor(msg[i:i+len(part_of_msg)], part_of_msg)
    if candidate.isalnum():
        print(candidate)

key = '0xBUETCTF'

print(xor(msg,key))

```

