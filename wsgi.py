from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Galih Hermawan"

@application.route('/user/<nama>')
def user(nama):
	#return render_template('user.html', nama=nama)
    return "Halo,", nama

if __name__ == "__main__":
    application.run()
