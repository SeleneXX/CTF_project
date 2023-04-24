from flask import Flask, render_template, request
import pymysql
from pymysql.constants import CLIENT

app = Flask(__name__)
conn = pymysql.connect(host="localhost", port=4306, user="root", passwd="asd12311", charset="utf8", db="ctf", client_flag=CLIENT.MULTI_STATEMENTS)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


@app.route("/admin/", methods=["GET", "POST", "PUT"])
def add_user():
    if request.method == "GET":
        if request.args.get("se") == "Happy_CTF":
            return render_template("python_reverse.html")

        return render_template("login.html")

    username = request.form.get("user")
    pwd = request.form.get("pwd")
    print(username)

    conn = pymysql.connect(host="localhost", port=4306, user="root", passwd="asd12311", charset="utf8", db="ctf")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = f"select * from admin where username='{username}' and password='{pwd}'"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    cursor.close()
    conn.close()
    print(data_list)
    if data_list:
        return render_template("check.html")
    else:
        return "Incorrect username or password"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
