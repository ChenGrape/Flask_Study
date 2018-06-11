"""
返回客户端的形式有两种
直接返回
1.响应体
    return "hello"
2. 响应体 + 状态码
   return "hello",666

3. 响应体 + 状态码 + 响应头
   return "hello",666,{"Content-Type":"application/json"}

手动创建response对象
response:返回给客户端内容的相应体对象
response = make_response("helloworld")
response.status = "999"
response.headers["Content-Type"] = "application/json"
return response
"""
from flask import Flask
from flask import make_response

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = make_response("helloworld")
    response.status = "999"
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    app.run(debug=True)