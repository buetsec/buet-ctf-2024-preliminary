
## Challenge: Inside
- **Difficulty**: Easy
- **Points**:
- **Author**: ShahRiffy

Bob: Where is the secret?

Jammy: Check Inside.

Bob: How ??

Jammy: Try with "1337BUET"

**File:** [inside.jpg](https://raw.githubusercontent.com/buetsec/buet-ctf-2024-preliminary/main/misc/Inside/inside.jpg)

**Flag:** `BUETCTF{Steganography_is_the_technique_of_hiding_data_within_an_ordinary}`


# Solve


`steghide extract -sf inside.jpg`

password = 1337BUET
