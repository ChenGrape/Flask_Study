"""
url_for():是flask中提供的一个方法
作用：可以通过视图函数的名称找到对应的路径
格式：url_for ('视图函数', key = value)
场景：一般用户服务器内部资源定位

redirect:重定向，自定定位到另外的资源
格式：redirect('路径')，内部的默认状态码
注意：使用url_for 传递参数，接收方需要与传递方完全一致
"""
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/taobao")
def taobao():
    return redirect("jingdong")

@app.route("/jingdong")
def jingdong():
    return "我有正品"


# 传参从定向
@app.route("/taobao2")
def taobao2():

    return redirect(url_for("jingdong2",num=100))

@app.route("/jingdong2/<int:num>")
def jingdong2(num):
    return "我有正品,%d块"%num

if __name__ == '__main__':
    app.run(debug=True)