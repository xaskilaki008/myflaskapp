from flask import Flask, render_template, send_from_directory, request, jsonify
import os

app = Flask(__name__)
FOLDER = "."  # Текущая папка

@app.route('/')
def index():
    files = []
    for item in os.listdir(FOLDER):
        path = os.path.join(FOLDER, item)
        files.append({
            "name": item,
            "is_dir": os.path.isdir(path),
            "size": os.path.getsize(path) if not os.path.isdir(path) else 0,
        })
    return render_template("index.html", files=files)

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)