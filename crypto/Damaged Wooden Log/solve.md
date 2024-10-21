#### Short Writeup

TODO

```python
from tqdm import tqdm
from Crypto.Util.Padding import unpad

p=113661483183599207666780369116478760871276423927132803405418082122587758493346987660116928155896918760533730362802627002308566750723206804302084761930855816675103149346004359320141206169305736089154645427652261031099756261117446871987551025288975427357052873914733538073915101574737774660429809674771810848271
y=8173116922439860088541141261289689960280327223117169708297806909529216065634883860226358008552279397824385117324142405165918261023886745883694230167315896195642203058616335618164407725448420238537687004123604889762806940652512992175530473289819350650365265304086443946832207875764837796425129498291389898140
ct='16db554562689e7f088efaa0daaaca7b09de0f9f365368b1201311f1392b19e0ae52b0f9b9786d94b77db07f29dd322207ed1fc99c5d7fec21bcb158f0ec1a65'
key=30287683382406630373983038341855903551063852746571598993640574228509616821481195198169199625250616175958766803781489854200998419394222315209116371708084015862431179054247135646674223693411838345904661420086287325773649043159011421283722269918524296653076356568543549825607815143576312752403032013609266909618

sz = 1024

pw = [1 for _ in range(sz)]
t = g
for i in range(1, sz):
  pw[i] = t
  t = (t * t) % p

negpw = [1 for _ in range(sz)]
ginv = pow(g, -1, p)
t = ginv
for i in range(1, sz):
  negpw[i] = t
  t = (t * t) % p

def getpow(e):
  if e < 0:
    return negpw[-e]
  else:
    return pw[e]

def decrypt(ct, key):
  return AES.new(hashlib.sha256(str(key).encode()).digest(), AES.MODE_ECB).decrypt(bytes.fromhex(ct))

y_ = pow(g, key, p)
h = (y * pow(y_, -1, p)) % p

print("[+] Precomputations done\nWill start doing first step of MITM")

keep = dict()
for b1 in tqdm(range(-sz + 1, sz)):
  for b2 in range(-sz + 1, sz):
    p1, p2 = getpow(b1), getpow(b2)
    prod = (p1 * p2) % p
    keep[prod] = (b1, b2)

print("[+] Frist step of MITM done\nWill start doing second step of MITM")

done = False
for b1 in tqdm(range(-sz + 1, sz)):
  if done:
    break
  for b2 in range(-sz + 1, sz):
    p1, p2 = getpow(b1), getpow(b2)
    prod = (p1 * p2) % p
    need = (h * pow(prod, -1, p)) % p
    if need in keep:
      b3, b4 = keep[need]
      print(f"\n{b1=}, {b2=}, {b3=}, {b4=}")
      fixed_key = key
      for b in [b1, b2, b3, b4]:
        b = abs(b) - 1
        fixed_key ^= (1 << b)
      print(f"{fixed_key=}")
      assert pow(g, fixed_key, p) == y
      msg = unpad(decrypt(ct, fixed_key), 16).decode()
      print(f"{msg=}")
      done = True
      break
```
