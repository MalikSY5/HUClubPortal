from flask import Flask, redirect, url_for, render_template

# app = Flask(__name__)

# @app.route("/")
# def home(): #signifies the home page of the website
#     # return "Hello! This is the main page <h1>HELLO</h1>"
#     return render_template("display.html", content = 'CEA BASKETBALL TOURNAMENT')
# @app.route("/<name>")
# def user(name): #function that displays the username
#     return f'Hello {name}!'

# @app.route('/admin')
# def admin(): #function that displays the admin name and redirects them to the hello page
#     return redirect(url_for('user', name = "Admin!"))

'''
        !!!!!!!!!!!R E A D M E!!!!!!!!!!!!!!

**THIS WAS MADE IN A PYTHON VIRTUAL ENVIRONMENT** if needed....
To activate the environment you must be inside the website Folder directory
Once inside the Directory type in this line into the terminal:.\WebEnv\Scripts\activate


HOW TO RUN THE FILE:
1. run the python Starter.py script inside the terminal
2. Ctrl + Click the link that is displayed inside the terminal or copy and paste the link into a browser URL.

**IMPORTANT** make sure at the end of the URL there is "/"



'''
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("roughdraft.html")

if __name__ == '__main__':
    app.run(debug=True)








# if __name__== '__main__':
#     app.run(debug = True)