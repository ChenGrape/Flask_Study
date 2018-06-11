"""
指定访问方式
格式：@app.route("路径",methods = ["方式一"，"方式二",...])
注意点：
1.多个访问方法】方式之间使用逗号隔开
2.常见访问方式：GET，POST，DELETE，PUT，DISPATCH，...等8种
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index1():
    return "index1"

@app.route('/',methods=["POST"])
def index2():
    return "index2"

if __name__ == '__main__':
    app.run(debug=True)