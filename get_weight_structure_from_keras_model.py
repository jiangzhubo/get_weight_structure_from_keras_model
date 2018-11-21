import os
import keras
import numpy as np
from keras.models import load_model
from keras.applications import mobilenet
from keras.utils.generic_utils import CustomObjectScope
from keras.models import model_from_json
import json

from skimage.transform import resize




path = ''
model = 'mobilenet'
#with CustomObjectScope({'relu6': mobilenet.relu6,'DepthwiseConv2D': mobilenet.DepthwiseConv2D}):
with CustomObjectScope({'relu6': keras.applications.mobilenet.relu6,'DepthwiseConv2D': keras.applications.mobilenet.DepthwiseConv2D}):
    model_path = pa
    model = load_model(model_path)
    json_string = model.to_json()
    weights = model.get_weights()
    np.save('keras_'+model+'_12classes',weights)
    with open('keras_'+model+'_12classes.json', 'w') as outfile:
         outfile.write(json_string)
