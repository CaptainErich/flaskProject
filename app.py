from flask import Flask,render_template,request
import datetime

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

@app.route('/index')
def hello():  # put application's code here
    return '222!'


@app.route('/user/<name>')
def welcom(name):  # put application's code here
    return '222!%s'%name


@app.route('/user/<int:id>')
def welcom1(id):  # put application's code here
    return '222!%d'%id

# @app.route('/')
# def index2():
#     return render_template("index.html")

@app.route('/')
def index2():
    time = datetime.date.today()
    name = ["小", "小JJ"]
    task = {"对吧": "value","对ee吧": "vaeeeelue"}
    return render_template("index.html",var = time, list=name, task = task)

@app.route('/test/register')
def register():
    return render_template("test/register.html")

@app.route('/relust',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form

    return render_template("test/relust.html", result=result )


if __name__ == '__main__':
    app.run()
