from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)


@app.route("/admin/", methods=["GET", "POST", "PUT"])
def add_user():
    if request.method == "GET":
        if request.args.get("se") == "Happy_CTF":
            return render_template("python_reverse.html")

        return render_template("login.html")

    username = request.form.get("user")
    pwd = request.form.get("pwd")
    print(username)

    # 1. 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="asd12311", charset="utf8", db="ctf")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2. 执行SQL
    sql = f"select * from admin where username='{username}' and password='{pwd}'"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    # 3. 关闭连接
    cursor.close()
    conn.close()
    print(data_list)
    if data_list:
        return render_template("check.html")
    else:
        return "Incorrect username or password"


if __name__ == '__main__':
    app.run()
