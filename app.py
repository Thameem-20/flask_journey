from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/About')
def About():
    return 'This is about page'

@app.route('/Contact')
def Contact():
    return 'This is Contact page'

if __name__ == "__main__":
    app.run(debug=True)
