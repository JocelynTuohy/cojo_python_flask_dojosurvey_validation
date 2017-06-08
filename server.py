from flask import Flask, render_template, request

# Hint: Although we've told you never to render from a post route, you'll need
# to do so for this assignment. We'll show you tools to avoid doing so soon.

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    dinosaur = request.form['dinosaur']
    beatle = request.form['beatle']
    return render_template('result.html', name=name, dinosaur=dinosaur,
                           beatle=beatle)

app.run(debug=True)
# Nothing after the debug line will be read.
