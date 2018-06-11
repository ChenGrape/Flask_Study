"""
request:请求对象，属于flask模块，里面封装了请求相关的内容
request.method
request.url
request.data
request.args
request.form
"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():

    print(request.method)
    print(request.url)
    print(request.args)

    return "helloworld"

if __name__ == '__main__':
    app.run(debug=True)