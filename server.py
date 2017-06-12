from flask import Flask, render_template, request, redirect, flash

# Hint: Although we've told you never to render from a post route, you'll need
# to do so for this assignment. We'll show you tools to avoid doing so soon.

app = Flask(__name__)
app.secret_key = "KeepItSecretButNotTooSecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    redirectBool = False
    print len(request.form['name'])
    if len(request.form['name']) < 1:
        flash("Name is a required field.")
        redirectBool = True
    if len(request.form['comment']) < 1:
        flash("Comment(s) are required.")
        redirectBool = True
    elif len(request.form['comment']) > 120:
        flash("Comment(s) may not exceed 120 characters.")
        redirectBool = True
    if redirectBool:
        return redirect('/')
    else:
        name = request.form['name']
        dinosaur = request.form['dinosaur']
        beatle = request.form['beatle']
        comment = request.form['comment']
        return render_template(
            'result.html',
            name=name,
            dinosaur=dinosaur,
            beatle=beatle,
            comment=comment)

app.run(debug=True)
# Nothing after the debug line will be read.
