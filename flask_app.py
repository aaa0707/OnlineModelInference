from flask import Flask, request, render_template, redirect, url_for
from src.utils import load_model, parse_read_data
from src.infer import execute_inference
from src.constants import model1_name, model2_name

import os


app = Flask(__name__)
project_dir = "tmp"

# define models during init so they aren't loaded for each request
model1 = load_model(os.path.join(project_dir, model1_name))
model2 = load_model(os.path.join(project_dir, model2_name))


@app.route('/file_data', methods=['POST'])
def result_file():
    """
    Flask based function that accepts a file (from flask.request) and runs inferencing on it 
    """
    f = request.files['input_file']
    data = parse_read_data(f.read().decode("utf-8"))
    results = execute_inference(model1, model2, data)

    return "\n".join(results)

@app.route('/upload')
def upload_page():
    """
    Flask based function that renders the uplaod page as a UI for file upload
    """
    return render_template('./upload.html')

@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file():
    """
    Flask based function that handles upload calls. This is wired in from the html used in "upload_page"
    If a POST request is called with the input file, the function returns the result using same codeflow as result_file
    If a GET request is called (user simply goes to this url), then it redirects to the upload page
    """
    if request.method == 'POST':
        return result_file()
    else:
        return redirect(url_for('upload_page'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
