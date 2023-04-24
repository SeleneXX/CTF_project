from flask import Flask, render_template, request, redirect
import pymysql
from pymysql.constants import CLIENT

app = Flask(__name__)
conn = pymysql.connect(host="localhost", port=4306, user="root", passwd="asd12311", charset="utf8", db="ctf", client_flag=CLIENT.MULTI_STATEMENTS)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

@app.route("/", methods=["GET"])
def info():
    return render_template("check.html")
@app.route("/login/", methods=["POST"])
def login():
    verification_code = request.form.get("verification_code")
    username = request.form.get("user")
    pwd = request.form.get("pwd")
    conn = pymysql.connect(host="localhost", port=4306, user="root", passwd="asd12311", charset="utf8", db="ctf")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = f"select username, password from admin where username='{username}' and password='{pwd}'"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    cursor.close()
    conn.close()
    print(data_list)
    if data_list and verification_code == "Happy_CTF":
        return redirect("/admin/")
    else:
        return "Incorrect username or password"




if __name__ == '__main__':
    app.run(host='0.0.0.0')
