from flask import Flask, render_template, request, redirect, url_for
import os
from skin_cancer_detection import detect_cancer

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        # Save the uploaded image
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(image_path)
        # Perform cancer detection
        result = detect_cancer(image_path)
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
