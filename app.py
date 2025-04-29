from flask import Flask, request, render_template, send_file
import torch
import tensorflow as tf
import os
import uuid
from optimizer.torch_optimizer import optimize_torch_graph
from optimizer.tf_optimizer import optimize_tf_graph
from optimizer.benchmark import benchmark_model

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OPTIMIZED_FOLDER = 'optimized'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OPTIMIZED_FOLDER, exist_ok=True)

def is_tensorflow_model(file):
    return file.filename.endswith('.pb')

def is_pytorch_model(file):
    return file.filename.endswith('.pt')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['model']
        if file:
            filename = str(uuid.uuid4())
            filepath = os.path.join(UPLOAD_FOLDER, filename)

            if is_pytorch_model(file):
                filepath += '.pt'
                file.save(filepath)
                optimized_path = optimize_torch_graph(filepath, OPTIMIZED_FOLDER)
                speedup = benchmark_model(filepath, optimized_path, framework='pytorch')
            elif is_tensorflow_model(file):
                filepath += '.pb'
                file.save(filepath)
                optimized_path = optimize_tf_graph(filepath, OPTIMIZED_FOLDER)
                speedup = benchmark_model(filepath, optimized_path, framework='tensorflow')
            else:
                return "Unsupported file format", 400

            return render_template('result.html', speedup=speedup, download_link=optimized_path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
