from flask import Flask, render_template, request

app = Flask(__name__, template_folder='view')


@app.route("/")
def index():
    html = render_template('index.html')
    return html


@app.route('/second', methods=['GET', 'POST'])
def second():
    data3 = request.values.get('data2')
    if request.method == 'POST':
        data1 = request.form['data1']
        data2 = request.form.get('data2')
        return f'data: {data1}, data2: {data2}, data3: {data3}'
    else:
        data1 = request.args['data1']
        data2 = request.args.getlist('data2')
        return f'data: {data1}, data2: {data2}, data3: {data3}'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
