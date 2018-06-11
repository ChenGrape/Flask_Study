"""
app应用程序对象加载配置信息的三个来源
1.从类的对象加载
2.从配置文件中加载
3.从环境变量中加载

"""

from flask import Flask

app = Flask(__name__)

class Config(object):
    DEBUG = True
# app.config.from_object(Config)

# 2.从配置文件中加载
app.config.from_pyfile("config.ini")

# 3.从环境变量中加载,不推荐使用
# app.config.from_envvar('FLASKCONFIG')

@app.route("/")
def hello_world():
    return "hello word!"

if __name__ == '__main__':
    print(app.config.get("DEBUG"))
    app.run()
