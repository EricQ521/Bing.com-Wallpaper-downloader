import requests
import json

# 必应壁纸API的URL
api_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"

# 发送GET请求获取壁纸信息
response = requests.get(api_url)
data = json.loads(response.text)

# 获取图片的URL
image_url = "https://cn.bing.com" + data["images"][0]["url"]

# 下载图片
image_data = requests.get(image_url).content
with open("bing_wallpaper.jpg", "wb") as file:
    file.write(image_data)

print("壁纸下载完成")