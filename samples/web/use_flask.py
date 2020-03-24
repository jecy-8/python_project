from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'

# Use template
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
# def singin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''

# Use template
def singin_form():
    return render_template("form.html")


@app.route('/signin', methods=['POST'])
# def signin():
#     if request.form['username'] == 'admin' and request.form['password'] == 'admin':
#         return '<h3>Hello Admin!</h3>'
#     return '<h3>Bad username and password</h3>'

# Use template
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin':
        return render_template('signin_ok.html', username=username)
    return render_template('form.html', message='Bad username and password', username=username)

if __name__ == '__main__':
    app.run()