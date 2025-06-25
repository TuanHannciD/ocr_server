from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import os

app = Flask(__name__)

# Thiết lập đường dẫn tessdata động, luôn đúng dù deploy ở đâu
tessdata_dir = os.path.join(os.path.dirname(__file__), 'tessdata')
os.environ['TESSDATA_PREFIX'] = tessdata_dir
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    img = Image.open(file.stream)
    # Nhận diện tiếng Việt
    text = pytesseract.image_to_string(img, lang='vie')
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000) 