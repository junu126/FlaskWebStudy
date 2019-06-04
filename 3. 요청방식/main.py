from flask import Flask, render_template, request

app = Flask(__name__, template_folder='view')


@app.route("/")
def index():
    html = render_template('index.html')
    return html


@app.route('/second', methods=['GET', 'POST'])
def second():
    # 요청 방식
    print('요청방식: { ' + request.method + ' }')

    # if request.method == 'POST'
    html = render_template('second.html')
    return html


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
