"""
在客户端访问后台的时候如何传递参数类型
格式：@app.route('路径/<数据类型：变量名>'
数据类型：
int     整数
float   小数
path    字符串，如果不指定path默认是字符串
"""

from flask import Flask

app = Flask(__name__)

@app.route("/<int:num>")
def int_route(num):
    return "the number is %s"%num

@app.route("/<float:num>")
def float_route(num):
    return "the number is %s"%num

@app.route("/<num>")
def path_route(num):
    return "the number is %s"%num

if __name__ == '__main__':
    app.run(debug=True)