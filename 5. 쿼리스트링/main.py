from flask import Flask, render_template, request

app = Flask(__name__, template_folder='view')


@app.route("/")
def index():
    return 'index'


@app.route('/test1')
def test1():
    return 'test1'


@app.route('/test1/sub1')
def test1_sub1():
    return 'test1 sub1'


@app.route('/test1/sub2')
def test1_sub2():
    return 'test1 sub2'


@app.route('/test2/<data1>')
def test2_data1(data1):
    return f'test2 data1: {data1}'


@app.route('/test2/<data1>/<data2>')
def test1_data1_data2(data1, data2):
    return f'test2 data1 data2: {data1} , {data2}'


@app.route('/test3')
@app.route('/test4')
def test3():
    return 'test3 or test4 sub1'


@app.route('/test5/<data1>')
def test2_data1(data1):
    return f'test5 data1: {data1}'


@app.route('/test5/<data1>/<data2>')
def test1_data1_data2(data1, data2):
    return f'test5 data1 data2: {data1} , {data2}'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
