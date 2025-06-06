python -m venv venv
source venv/bin/activate  # Windowsなら venv\Scripts\activate
pip install flask

from flask import Flask, render_template, request

app = Flask(__name__)

# ごみ分別データ例
GOMI_DICT = {
    "ペットボトル": "資源ごみ",
    "生ごみ": "燃えるごみ",
    "缶": "資源ごみ",
    "古紙": "資源ごみ",
    "ガラス瓶": "資源ごみ",
    "電池": "有害ごみ",
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bunbetsu', methods=['GET', 'POST'])
def bunbetsu():
    result = None
    if request.method == 'POST':
        item = request.form.get('item')
        result = GOMI_DICT.get(item, "ごみの種類が登録されていません。")
    return render_template('bunbetsu.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html>
<head>
    <title>ごみ分別アプリ</title>
    <style>
        .button {
            width: 200px;
            height: 100px;
            font-size: 24px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            margin: 50px auto;
            display: block;
        }
    </style>
</head>
<body>
    <button class="button" onclick="location.href='/bunbetsu'">ごみの分別</button>
</body>
</html>
<!DOCTYPE html>
<html>
<head>
    <title>ごみの分別ページ</title>
</head>
<body>
    <h1>ごみの種類を入力してください</h1>
    <form method="POST">
        <input type="text" name="item" placeholder="例：ペットボトル" required>
        <button type="submit">調べる</button>
    </form>

    {% if result %}
    <h2>結果: {{ result }}</h2>
    {% endif %}

    <button onclick="location.href='/'">戻る</button>
</body>
</html>
