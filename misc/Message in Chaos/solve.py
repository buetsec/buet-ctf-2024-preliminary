f = open('enc.buet')
seen = {}
  
for line in f:
    for character in line:
        if character in seen:
            seen[character] += 1
        else:
            seen[character] = 1

for key in seen:
    print(chr(seen.get(key)), end="")
print()