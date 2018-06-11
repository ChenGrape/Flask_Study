"""
之所以可以通过int,float等数据类型内容是因为吸收通已经提供了默认的转换器
如果需要实现复杂的过滤操作，需要自定义转换器
定义使用步奏
1.自定义类，继承自BaseConverter
2.编写__init__方法，接收两个参数，初始化父类
3.将规则赋值给子类对象
4.将自定义的转换器添加到系统默认的转换器列表中

to_python:屁【匹配成功之后，执行视图函数之前，可以过滤一些数据，编码转换工作
"""

from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class MyRegexConverter(BaseConverter):
    # regex = '\d{3}'

    def __init__(self,url_map,regex):
        super(MyRegexConverter, self).__init__(url_map)
        self.regex = regex

app.url_map.converters["re"] = MyRegexConverter
print(app.url_map.converters)

@app.route("/<re('\d{3}'):num>")
def hello_world(num):
    return "the num is %s"%num

@app.route("/<re('1[356789]\d{9}'):mobile>")
def get_phonenumber(mobile):
    return "the mobile is %s"%mobile

if __name__ == '__main__':
    app.run(debug=True)