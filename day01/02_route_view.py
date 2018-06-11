"""
1.如果一个路由绑定多个视图函数，优先访问的是先装饰的
2.如果多个路由绑定多个视图函数，通过所有的路径都可以访问
"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index1():
    return "index1"

@app.route("/")
def index2():
    return "index2"

@app.route("/index1")
@app.route("/index2")
@app.route("/index3")
def index3():
    return "index3"

if __name__ == '__main__':
    app.run(debug=True)

