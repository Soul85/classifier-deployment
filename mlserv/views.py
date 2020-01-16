from flask import render_template, redirect, request, jsonify
from werkzeug.utils import secure_filename
from keras.preprocessing import image
from mlserv import app, model
from .forms import ImageForm
import numpy as np

@app.route('/')
def home():
    """Renders the home page using the base index template."""
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predictor():
    """Handles rendering of the prediction page and POST data to that page after submission."""
    # Instantiates the ImageForm object from the forms file
    form = ImageForm()
    # Checks if form submission is valid or not
    if form.validate_on_submit():
        img = image.img_to_array(image.load_img(form.img.data, target_size=(64, 64)))
        img = np.expand_dims(img, axis=0)
        if model.predict(img)[0][0] == 1:
            result = 'Dog'
        else:
            result = 'Cat'
        # Returns the prediction result if the form submission was valid
        return render_template('predict.html', result=result)
    # If there is no form submission or if it is not valid, render the submission page normally
    return render_template('predict.html', form=form)