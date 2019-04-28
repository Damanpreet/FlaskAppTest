from flask import Flask
app_test = Flask(__name__)

#Flask puts the server on port 5000 by default.
@app_test.route('/hello_page')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app_test.run(debug=True)
