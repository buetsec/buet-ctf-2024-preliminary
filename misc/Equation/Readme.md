## Challenge: Equation
- **Difficulty**: Easy
- **Points**:
- **Author**: ShahRiffy

a = SSH + HTTP + UPS
b = RDP - SLP
c = (Telnet + FTP) * SMTP
d = STUN * Echo

flag = c(b -a) + d


**Flag:** `BUETCTF{2729246}`





# Solve

After converting all of the protocols to their respective port numbers, here is what the math should look like:

a = SSH + HTTP + UPS = 22 + 80 + 401 = 503
b = RDP - SLP = 3389 - 427 = 2962
c = (Telnet + FTP) * SMTP =(23 + 21) * 25 = 1100
d = STUN * Echo = 3478 * 7 = 24346


flag = c(b -a) + d = 1100(2962 - 503) + 24346 = 2729246
