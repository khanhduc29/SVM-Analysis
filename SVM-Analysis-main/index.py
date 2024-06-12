from flask import Flask, render_template

app = Flask(__name__)


@app.route('/duc')
def summary():
    return render_template('index.html')
@app.route('/')
def home():
    return "Hello!, Flask"

if __name__ == '__main__':
    app.run(debug=True)
