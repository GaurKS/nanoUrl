from flask import Flask, request, redirect
import string
import random

app = Flask(__name__)
url_dict = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = shorten_url()
        url_dict[short_url] = long_url
        return f'Shortened URL: {request.host_url}{short_url}'
    return '''
        <form method="post">
            <label for="long_url">Enter the URL to shorten:</label><br>
            <input type="text" name="long_url" id="long_url" required><br>
            <input type="submit" value="Shorten URL">
        </form>
    '''

@app.route('/<short_url>')
def redirect_url(short_url):
    if short_url in url_dict:
        return redirect(url_dict[short_url])
    else:
        return f'Invalid URL'

def shorten_url():
    chars = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(chars) for _ in range(6))
    while short_url in url_dict:
        short_url = ''.join(random.choice(chars) for _ in range(6))
    return short_url

if __name__ == '__main__':
    app.run(host='0.0.0.0')