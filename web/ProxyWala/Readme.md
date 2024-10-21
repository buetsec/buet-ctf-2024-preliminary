# Name: Proxy Wala
## Category: Web
## Difficulty: Medium (250-150 dynamic)

Mr. John created a Proxy Server to view web contents. He claims it is a secure server and that no one can hack it.

Your challenge is to view `/secret/flag.html`.

**Link:** https://web-challs1.buetctf.xyz/proxywala/
**Author**: [Oxf4h1m](https://fb.com/fa11m)  
**Attachment**: [proxywala.zip](https://drive.google.com/file/d/1xj1HsGFRAmbkWefXasTRZxsv_Kr5RQUk/view?usp=sharing)

### Flag: 
`BUETCTF{W0W!!_r3ad_f1l3_fr0m_s3rv3r_using_lf1}`

### solution: 
payload `file://2130706433/secret/fl../ag.html` 

read the sourcecode from attachment then analyze the filter 
```
def validate_url(url):

    # Blocking File read
    if url.startswith("/") or url.startswith("file:///"):
        return False
    # Add further checks for SSRF or malicious inputs here
    if "localhost" in url or "0.0" in url:
        return False
    return True
```

and 

```
            if 'flag' in url :
                return render_template('403.html', reason="No flag 🚩. No Victory")
            url = url.replace("../", "")
```
