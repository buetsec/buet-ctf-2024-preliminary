## Isshin the sword saint

This is the `sword.py` script we are given with:

```py
import random

flag = b'BUETCTF{...}'
flag = flag.lstrip(b'BUETCTF{').rstrip(b'}')
assert all(65 < c < 125 for c in flag)

M = 10**9 + 7
e = 69420

seq = []
for c in flag:
  e = e + random.randint(69, 420)
  o = (c * pow(2, e, M)) % M
  seq.append(o)

random.shuffle(seq)
print(seq)

#[173941810, 858898665, 468848314, 635867560, 633540626, 16418674, 294931476, 461014, 350360176, 294627774, 552498858, 886470836, 828069064, 432658831, 341519287, 320474506, 598269374, 967937144, 418635091, 399599765, 983033996, 703488819, 58442600, 257836528, 241409305, 811247888, 442468084, 199395519, 579859752, 112962212, 816269013, 9496448, 249252133, 927028574]
```
The following happens in order:
* The flag is stripped of it's known prefix and suffix before it is further modified. 
* For each character $c$, it is changed to to $o = c \cdot 2^e \mod M$ where $e = 69420 + k$ and $k$ is some random number between ($69, 420$). Note that $e$ is an ever increasing number which, at every iteration, increaes by a random bound ($69, 420$).
* This new sequence generated is then shuffled in a random manner and given to the players.

So each transformed character in the flag can accurately be written as $o_i = c_i \cdot 2^{e_i} \mod M$ where $e_i = 69420 + \sum_{i=1}^{n} k_i$ and $69 \le k_i \le 420$. It is important to understand the case of $e$. Note that initially $e = 69420$. Then at each iteration, it is added to a random number $k_i$. So if at the first iteration, $e_1 = 69420 + k_1$, at the second iteration, it will become $e_2 = 69420 + k_1 + k_2$, and so it keeps on icreasing. Hence the $\sum_{}^{} k_i$ part is added to $e$. 

### Recovering each $c_i$

From the sufffled output, we will recover the original characters that constituted the flag. We can re-write the previous equation as, $c_i = o_i * 2^{-e_i} \mod M$, where the $e_i$ is unknown. Only if we could guess $e_i$, we could have obtained each $c_i$.

Well, $e_i = 69420 + \sum_{i=1}^{n} k_i$ and where $k_i$ can't be more than $420$. So if the flag consists of $50$ characters, $e_i$ can be maximum of $69420 + 50*420 = 90420$. This is very well in the brute-forceable region. That is, for a $50$ character flag, $69420 \le \sum_{i=1}^{50} k_i \le 90420$. So let's try all values of $e_i$ from $69420$ upto $90420$ and eventually for the right value, we will get the right $c_i$.

But, how do we know that we have found the right $c_i$? There could be multiple valid values right? Actually ... no. There won't be more than one valid value. This is ensured by the line `assert all(65 < c < 125 for c in flag)`. Because of this, we are guaranteed that $64 < c_i < 128$, or $2^6 < c_i < 2^7$. At the brute force that we are doing, we are simply dividing $o_i$ by powers of $2$ (modular division), so we will get the valid value if and only if we are within the bound (exclusive) $(64, 128)$, ensuring unique values. 

**Make sure to note down each $e_i$ as it will be required in the next step**

### Reordering the shuffled flag

Thanks to the previous step, we have the flag characters, but shuffled. We need to reorder them. Remember I mentioned that the $e_i$ values are strictly increasing, that is $e_1 < e_2 < e_3 < \cdots < e_n$. As we have noted down the $e_i$ values from the previous step, we are going to use them to permute or reshuffle the flag. Suppose that we have $(c_i, e_i) = ('m', 72340)$ and $(c_{i+1}, e_{i+1}) = ('k', 69880)$, it is intuitive that $k$ must come before $m$ as $e_{i+1} < e_i$. In this way the whole flag can be reordered.

> BUETCTF{Who_lEt_thE_aUtHor_cOoK_hUh_Oo_zZz}

```python
seq = [173941810, 858898665, 468848314, 635867560, 633540626, 16418674, 294931476, 461014, 350360176, 294627774, 552498858, 886470836, 828069064, 432658831, 341519287, 320474506, 598269374, 967937144, 418635091, 399599765, 983033996, 703488819, 58442600, 257836528, 241409305, 811247888, 442468084, 199395519, 579859752, 112962212, 816269013, 9496448, 249252133, 927028574]
m = []
einv_ = pow(2, -69420, M)
twoinv = pow(2, -1, M)

for o in seq:
  einv = einv_
  itr = 0
  while True:
    c = (o * einv) % M
    if 65 < c < 125:
      m.append((itr, c))
      break
    einv = (einv * twoinv) % M
    itr += 1

m.sort()
m = 'BUETCTF{' + ''.join(chr(c) for _, c in m) + '}'
```

---
