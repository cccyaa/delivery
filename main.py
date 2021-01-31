from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/hi/<value>')
def hi(value):
    return 'Hi, {}'.format(value)

@app.route('/bye/<value>')
def bye(value):
    return 'bye, {}'.format(value)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
