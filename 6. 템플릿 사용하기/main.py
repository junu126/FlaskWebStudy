from flask import Flask, render_template, request
app = Flask(__name__, template_folder='view')


@app.route('/')
def second():
    test_dic = {
        'a1': 100,
        'a2': '문자열'
    }

    test_list = (10, 20, 30, 40, 50)

    html = render_template(
        'index.html', data_dic=test_dic, data_list=test_list)
    return html


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
