from flask import Flask, redirect, url_for, render_template, request, flash
from flask import request, session


app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def foo():
    return render_template('ass6.html')


@app.route('/userList')
def userList():
    return render_template('userList.html')


@app.route('/assignment8')
def assignment8():
    my_hobbies = ['singing', 'cooking', 'playing']
    name = "danielle"
    return render_template('assignment8.html', my_hobbies=my_hobbies, name=name)


@app.route('/assignment9', methods=['GET', 'POST'])
def ass9():
    Fname, Lname, Email = None, None, None
    Nname, Pword = None, None

    users = [{"Email": "danielleb9910@gmail.com", "First_name": "Danielle", "Last_name": "Bentov"},
             {"Email": "lindsay.ferguson@reqres.in", "First_name": "Lindsay", "Last_name": "Ferguson"},
             {"Email": "tobias.funke@reqres.in", "First_name": "Tobias", "Last_name": "Funke"},
             {"Email": "byron.fields@reqres.in", "First_name": "Byron", "Last_name": "Fields"}]

    if request.method == 'GET':
        if request.args:
            Fname = request.args['First_name']
            Lname = request.args['Last_name']
            Email = request.args['Email']
    if request.method == 'POST':
        Nname=request.form['N']
        Pword=request.form['P']
        session["login"]=True
        session["name"]=Nname

    return render_template('assignment9.html', users=users, Fname=Fname, Lname=Lname, Email=Email, Pword=Pword,
                           Nname=Nname)


@app.route('/blockExample')
def extend_of_assignment8():
    my_hobbies = ['singing', 'cooking', 'playing']
    name = "danielle"
    return render_template('blockExample.html', my_hobbies=my_hobbies, name=name)


if __name__ == '__main__':
    app.run(debug=True)