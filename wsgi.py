from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template('index.html')
    #return "Galih Hermawan"

@application.route('/user/<nama>')
def user(nama):
    return render_template('user.html', nama=nama)

if __name__ == "__main__":
    application.run()
