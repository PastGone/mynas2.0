import os
import random

from flask import Flask, render_template

# 导入该库用于发送邮件信息

app = Flask(__name__, static_folder="./static")

# 这里的folder_path是要扫描的文件夹
# 要求的话必须放在该项目下 否则的话会报错

folder_path = 'static/movie/bluevideo'


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/list/')
def myfilelist():
    # os.walk(path) 是 Python 中的一个函数，用于遍历指定路径下的所有文件和文件夹。
    # 它返回一个生成器对象，每次迭代时，
    # 会返回一个三元组 (当前文件夹路径, 当前文件夹中的子文件夹列表, 当前文件夹中的文件列表)。

    for root, dirs, files in os.walk(folder_path):
        return render_template("list.html", files=files)


@app.route('/name/<file>')
def plyer_page(file):
    filename = os.path.basename(file)
    print(filename)
    return render_template("player6.html", file=file, filename=filename)


@app.route('/manage/')
def manage():
    return "当前页面未开发"


@app.route("/fun_tools/")
def fun():
    return render_template("fun_tools.html")


@app.route("/fun_tools/beauty/")
def beauty():
    import json

    datas = ""
    with open('yuan.json', 'r') as f:
        datas = json.load(f)

        for data in datas:
            random_video = random.choice(data)
            return render_template("beauty.html", video=random_video)


@app.route("/link/")
def beauty_api():
    return  "当前页面未开发"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
