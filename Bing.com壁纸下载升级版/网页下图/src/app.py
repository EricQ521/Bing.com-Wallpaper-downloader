import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_wallpaper', methods=['POST'])
def download_wallpaper():
    api_url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
    response = requests.get(api_url)
    data = json.loads(response.text)
    image_url = "https://cn.bing.com" + data["images"][0]["url"]
    return image_url

if __name__ == '__main__':
    app.run(debug=True)
