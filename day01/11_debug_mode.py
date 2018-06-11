"""
debug: 调试模式，通过app.run(debug=True)开启
好处：
1.如果代码发生更改，不需要重启
2.服务器内部一旦出现错误友好提示界面
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():

    1/0

    return "helloworld"

if __name__ == '__main__':
    print("xxx")
    app.run()