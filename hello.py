from flask import Flask, render_template
#export FLASK_APP=[YOUR_APP_FILE].py  ( in command line)
#$ flask --app hello run --debug
#Create a Flask Instance
app=Flask(__name__)

#Create a route decorator
@app.route('/')
def index():
	first_name="John"
	stuff="This is <strong> Bold </strong> text"
	favorite_pizza=["cheese","broccoli"]
	return render_template("index.html",first_name=first_name,stuff=stuff,favorite_pizza=favorite_pizza)
	# return "<h1>Hello World</h1>"

#Filters
# safe
# capitalizt
# PackOverflowErrorupper
# title --used to capitalize the first letter of each word
# trim
# striptags

#localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
	return render_template("user.html",user_name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500





# if __name__ == '__main__':
#     app.run(host='0.0.0.0')