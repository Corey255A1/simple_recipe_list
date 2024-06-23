# WunderVision 2024
# Present the user with a list of PDFs of recipes

from flask import Flask, render_template, send_from_directory
import os
import pathlib
import re

RECIPES_DIR = './recipes';

app = Flask(__name__)

def find_all(path, extension):
    files = os.listdir(path)
    ext_filter = lambda file:re.search(f'\\.{extension}+$', file, re.IGNORECASE) != None
    full_file_names = list(filter(ext_filter, files))
    file_names = [pathlib.Path(file).stem for file in full_file_names]
    file_list = list(zip(full_file_names, file_names))
    file_list.sort(key=lambda x: x[1])
    return file_list

current_recipe_list = list(find_all(RECIPES_DIR, 'pdf'))


@app.route('/recipes/<filename>')
def get_recipe(filename):
    return send_from_directory(RECIPES_DIR, filename)

@app.route('/')
def index():
    # List all files in the current directory
    return render_template('index.html', files=current_recipe_list)

if __name__ == '__main__':
    app.run(debug=True)

