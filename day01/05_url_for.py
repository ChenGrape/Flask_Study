"""
url_for():是flask中提供的一个方法
作用：可以通过视图函数的名称找到对应的路径
格式：url_for ('视图函数', key = value)
场景：一般用户服务器内部资源定位
"""

from flask import Flask, url_for

app = Flask(__name__)

@app.route("/banzhang")
def banzhang():
    return "我没钱，找<a href='%s'>副班长</a>"%url_for("fubanzhang")

@app.route('/fubanzhang')
def fubanzhang():
    return "我是富班长,借你9块钱"

if __name__ == '__main__':
    app.run(port=5400, debug=True)