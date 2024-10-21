from flask import Flask, request, render_template, abort
import urllib.parse
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

app = Flask(__name__)

# Define allowed protocols and validation rules
def validate_url(url):

    # Blocking File read
    if url.startswith("/") or url.startswith("file:///"):
        return False
    # Add further checks for SSRF or malicious inputs here
    if "localhost" in url or "0.0" in url:
        return False
    return True

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            url = request.form.get('url')
            
            if 'flag' in url :
                return render_template('403.html', reason="No flag 🚩. No Victory")
            url = url.replace("../", "")
            
            if not validate_url(url):
                return render_template('403.html', reason="Malicious URL detected (SSRF, etc.)")
            
            try:
                content = urlopen(url, timeout=2).read().decode('utf-8')
                return render_template('content.html', content=content, url=url)
            except (URLError, HTTPError) as e:
                return render_template('403.html', reason=f"Error fetching URL. Possibly malicious.{e}")

        return render_template('index.html')
    except Exception as e:
        # Handle any fetch error with a generic funny error
        abort(500, description=f"Error 500: Something broke while fetching {url}. Oopsie! 😂")

# Error page
@app.errorhandler(403)
def error_403(e):
    return render_template('403.html', reason="403 Forbidden"), 403
# Custom 403 error page


# Custom 500 error page
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html', message=e.description), 500
if __name__ == '__main__':
    app.run(debug=True)
