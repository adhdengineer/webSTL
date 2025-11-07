import os
import argparse
from flask import Flask, jsonify, render_template, send_from_directory
from file_lister import scan_directory

# Parse command-line arguments
parser = argparse.ArgumentParser(description='STL Viewer Web Server')
parser.add_argument('--model-dir', type=str, required=True, help='Path to directory containing STL files')
args = parser.parse_args()

STL_DIR = os.path.abspath(args.model_dir)
if not os.path.isdir(STL_DIR):
    raise ValueError(f"Provided model directory does not exist: {STL_DIR}")

SCRIPTS_DIR = 'scripts'

# Normalize and validate path

app = Flask(__name__)


@app.route('/')
def index():
    files = []
    for f in os.listdir(STL_DIR):
        if f.lower().endswith('.stl'):
            #create_preview(f)
            files.append(f)
    return render_template('index.html')
    
@app.route('/filetree')
def filetree():
    return jsonify(scan_directory(STL_DIR, STL_DIR))

   
@app.route('/stls/<path:filename>')
def serve_file(filename):
    return send_from_directory(STL_DIR, filename)
    
@app.route('/scripts/<path:filename>')
def serve_scripts(filename):
    return send_from_directory(SCRIPTS_DIR, filename)


if __name__ == '__main__':
    app.run(debug=True)