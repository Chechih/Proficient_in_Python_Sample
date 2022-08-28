from flask import Flask, render_template

app = Flask(__name__)

@app.route('/echo/<thing>')
def echo(thing):
    return render_template('flask2.html', thing=thing)

app.debug = True#VS Code debuger 用
app.run(port=9999, debug=True)
