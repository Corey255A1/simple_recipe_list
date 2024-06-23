from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/recipe/<filename>')
def get_recipe(filename):
    return send_from_directory('./', filename)

@app.route('/')
def index():
    # List all files in the current directory
    files = os.listdir('.')
    return render_template('index.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)
