### Challenge Name : Agent Martin
### Challenge Category : Web
### Challenge Level : Easy
### Flag :
``BUETCTF{0nly_1n5ider5_are_All0w3d_t0_kn0w_ab0ut_th3_53cr3t5}``

### Challenge Description:
I've been following Agent Martin for a long time and I tried to learn about their secret missions. But I failed every time because they only share informations with the insiders of their organization. Can you help me to get some of their secrets?

**Link:** http://68.183.231.67/agent_martin/
### Instruction for Hosting :

- Do not host the challenge behind any CDN or Firewall.

### Solution : 
``curl -H "User-Agent: Martin" -H "X-Forwarded-For: 127.0.0.1" <Challenge_Host>``