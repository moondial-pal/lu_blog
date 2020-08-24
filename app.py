from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def blog():
	return render_template("blog.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")