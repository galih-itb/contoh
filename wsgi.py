from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    render_template('index.html')

@application.route('/user/<nama>')
def user(nama):
    return render_template('user.html', nama=nama)

if __name__ == "__main__":
    application.run()
