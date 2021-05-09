from datetime import datetime
from flask import Flask,render_template,request
from flask.globals import session
import hashlib
import json

app = Flask(__name__)
app.secret_key = "myself"

#ダミーデータ
chatData = [
    {"name":"0","message":"こんにちは！"},
    {"name":"1","message":"こんにちは！！！"}
    ]

@app.route("/")
def index():
    #ユーザー識別番号の確認
    if "userId" not in session:
        session["userId"] = hashlib.sha256(
            str(datetime.now().timestamp()).encode()
            ).hexdigest()[:10]
    myName = session["userId"]
    #クエリパラメータの確認と処理
    if "message" in request.args.keys():
        chatData.append({
            "name":myName,
            "message":request.args.get("message")
        })
    print(chatData)
    return render_template("index.html",chatData=chatData,myName=myName)

@app.route("/check_update")
def checkUpdate():
    return json.dumps({"chatSize":len(chatData)})

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")