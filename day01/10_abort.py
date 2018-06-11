"""
abort(代号):主动抛出异常异常代号信息
raise(异常对象)
会配合@app.errorhandler(代号/对象）使用，做自定义错误页面的提示
"""
from flask import Flask,abort


app = Flask(__name__)

@app.route("/")
def hello_world():

    # abort(403)
    # raise(Exception("大异常!!!"))

    1/0
    return "hello word!"

@app.errorhandler(403)
def exception_403(e):

    return "你的权限不够,禁止访问该方法"

@app.errorhandler(Exception)
def exception(e):

    print(e)

    return "大异常,出现了"

if __name__ == '__main__':
    app.run(debug=True)