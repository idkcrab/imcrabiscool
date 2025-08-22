from flask import Flask, render_template, request, redirect, url_for
import json
import string, random, os

app = Flask(__name__)

URL_FILE = "urls.json"

# Load URLs
if os.path.exists(URL_FILE):
    with open(URL_FILE, "r") as f:
        urls = json.load(f)
else:
    urls = {}

# Generate random short code
def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choice(chars) for _ in range(length))
        if code not in urls:
            return code

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form.get("url")
        if original_url:
            code = generate_code()
            urls[code] = original_url
            with open(URL_FILE, "w") as f:
                json.dump(urls, f)
            short_url = request.host_url + code
            return render_template("short.html", short_url=short_url)
    return render_template("short.html")

@app.route("/<code>")
def redirect_url(code):
    if code in urls:
        return redirect(urls[code])
    return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)
