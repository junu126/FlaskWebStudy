import json
from flask import Flask, render_template, request
app = Flask(__name__, template_folder='view')


@app.route('/')
def second():
    test_dic = {
        'a1': 100,
        'a2': '문자열'
    }

    json_data = json.dumps(test_dic, indent=4, ensure_ascii=False)
    # indent는 들여쓰기, ensure_ascii는 한글 처리

    print(json_data)

    python_data = json.loads(json_data)
    print(python_data)
    print(type(json_data))
    print(type(python_data))
    return json_data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
