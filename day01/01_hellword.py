"""
1. 导入Flask类所在的模块
2.创建队形，可以传递参数
3.通过路由路径绑定视图函数
4.启动应用该程序
"""
from flask import Flask

# __name__:表示当前程序启动的模块，如果是当前模块，值为：__main__,如果是其他模块调用的，那么名称是模块名称
# static_url_path: 表示静态资源的路径： / + static
# static_folder: 默认是static，静态资源的文件夹
# template_folder: 模板文件夹，默认值是templates


app = Flask(__name__)
print(app.static_folder)
print(app.static_url_path)
print(app.template_folder)

@app.route("/")
def index():
    return "index"

if __name__ == '__main__':
    # 启动应用程序，默认的ip是127.0.0.1 或者是0.0.0.0 默认端口是：5000
    # 更改绑定app.run(host="127.0.0.1", port=5001)
    app.run()