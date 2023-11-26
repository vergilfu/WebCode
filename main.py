from flask import Flask, jsonify, request
from flask_cors import CORS
import gptmethod

app = Flask('Couples homepage')
CORS(app)  # 处理跨域请求


@app.route('/gpt/<path:path>', methods=['GET','POST'])
def gptrou(path):
    if path == 'chat/getanswer':
        data = request.get_json()
        return gptmethod.getanswer(data=data)






if __name__ == '__main__':
    app.run(host='192.168.1.10',port=8085)