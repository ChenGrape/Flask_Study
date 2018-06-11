"""
url_map :可以查看当前的应用程序app中已经绑定了那些视图函数和路由之间的映射关系
格式：app.url_map: 返回的是一个map集合
"""

from flask import Flask

app = Flask(__name__)

@app.route('/hello_world')
def hello_world():

    return "helloworld"

@app.route('/index1', methods=["post"])
@app.route('/index2')
def index2():

    return "index2"

if __name__ == '__main__':

    print(app.url_map)
    app.run(debug=True)