from __future__ import division, print_function
#Flask App
import os
import numpy as np

# Keras
from keras.applications.imagenet_utils import preprocess_input
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

upload_folder = os.path.join(os.path.dirname(__file__), 'uploads')
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

app.config['UPLOAD_FOLDER'] = upload_folder

MODEL_PATH = 'models/resnet50_model.h5'

model = load_model(MODEL_PATH)

print('ResNet50 Model is loaded. Live at : http://127.0.0.1:5000/')

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    return preds

@app.route('/', methods=['GET'])
def index():
    
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        
        f = request.files['file']

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(file_path)

        preds = model_predict(file_path, model)

        # Process your result for human
        if preds.shape[1] == 2:
            # Binary classification
            pred_class = 'The skin lesion has melanoma skin cancer.' if preds[0][1] > 0.5 else 'The skin lesion does not have melanoma skin cancer.'
        else:
            # Adjust for other types of outputs if needed
            pred_class = 'Unknown'

        return pred_class
    return None

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)