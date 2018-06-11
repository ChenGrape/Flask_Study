"""
后台向客户端（浏览器，手机app,ipad,电子设备）返回数据的时候，往往需要制定数据格式
有两种方式指定jsons格式：
jsonify(dict)
json.dumps(dict),需要配合response，设置Content—Type
"""
from flask import Flask, jsonify,json,make_response

app = Flask(__name__)

@app.route("/")
def hello_world():

    # 1.jsonify(dict)
    dict = {
        "name":"zhangsan",
        "age":13
    }
    return jsonify(dict)
    # return jsonify(name="lisi",age=14)

    # 2.json.dumps(dict), 需要配合response, 设置Content - Type
    response = make_response(json.dumps(dict))
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    app.run(port=4654,debug=True)