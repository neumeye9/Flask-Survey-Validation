from flask import Flask, render_template, session, flash, request, redirect
app = Flask(__name__)
app.secret_key = "k1313k"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/info', methods=['POST'])
def info():
    name = request.form['name']
    dojo = request.form['dojo']
    language = request.form['language']
    comments = request.form['comments']

    if len(name) < 1:
        flash("Name cannot be empty!")
        return render_template('index.html')
    if len(comments) < 1:
       flash("Comments cannot be empty")
       return render_template('index.html')
    elif len(comments)>120:
        flash("Comments cannot be longer than 120 characters")
        return render_template('index.html')
    return render_template('info.html',name=name,dojo=dojo,language=language, comments=comments )




app.run(debug=True)