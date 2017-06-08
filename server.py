from flask import Flask, render_template, request, redirect

# Hint: Although we've told you never to render from a post route, you'll need
# to do so for this assignment. We'll show you tools to avoid doing so soon.

app = Flask(__name__)

@app.route('/')
def ():
    return render_template('index.html')

app.run(debug=True)
# Nothing after the debug line will be read.
