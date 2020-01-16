# Dog-Cat Image Classifier
This is a Flask web server deployed CNN model that classifies images that contain a dog or a cat.

I have effectively brought the accuracy of this model up to 94% training data accuracy with a 0.14 loss and 88% validation data accuracy with a 0.31 loss after 3 total training phases. The initial training phase was 100 training and validation steps per epoch with 10 epochs as a baseline I used to compare against previous model versions. The following two training phases were focused on training the model with the standard (sample_size / batch_size) configuration.

Regarding the validation loss, it was kept stable between 0.2 and 0.4.
