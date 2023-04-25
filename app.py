from flask import Flask, render_template, request, Response, jsonify
import json
import pymysql
from pymysql.constants import CLIENT

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main_page():
    return render_template("mainpage.html")

@app.route("/check/", methods=["GET"])
def info():
    search = request.args.get('id')
    conn = pymysql.connect(host="172.18.0.3", port=3306, user="root", passwd="abc123456", charset="utf8", db="ctf")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    datalist = {}
    if search:
        sql = f"select * from product_id where id='{search}'"
        cursor.execute(sql)
        data = cursor.fetchone()
        datalist[0] = data
        return Response(json.dumps(datalist), mimetype='application/json')
    sql = f"select * from product_id"
    cursor.execute(sql)
    data = cursor.fetchall()
    for idx, dic in enumerate(data):
        datalist[idx] = dic
    return Response(json.dumps(datalist), mimetype='application/json')

@app.route("/login/", methods=["POST"])
def login():
    verification_code = request.form.get("secretcode")
    username = request.form.get("username")
    pwd = request.form.get("password")
    if username and pwd and verification_code:
        conn = pymysql.connect(host="172.18.0.3", port=3306, user="root", passwd="abc123456", charset="utf8", db="ctf")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select username, password from admin where username=%s and password=%s"
        cursor.execute(sql, [username, pwd,])
        data_list = cursor.fetchone()
        cursor.close()
        conn.close()
        if not data_list:
            return "Incorrect username or password"
        if verification_code != "Happy_CTF":
            return "Incorrect secret code"
        return render_template("admin.html")

    return "You need to fill all the fields for login."

@app.route("/asdersfchangntsncot.pyc/", methods=["GET"])
def flag():
    flag_dict = {
        "msg": "Congrats, here is the flag!",
        "flag": "flag{Happy_CTF_CS561}"
    }
    return jsonify(flag_dict)




if __name__ == '__main__':
    app.run(host='0.0.0.0')
