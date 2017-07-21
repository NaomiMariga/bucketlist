from flask import Flask, render_template

app = Flask('__name__')

@app.route('/index/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['GET'])
def register():
    return render_template('register.html')

if __name__ == "__main__":
    app.run()
