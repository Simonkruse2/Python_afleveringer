import os, re, math, json, shutil, pprint
import PIL.Image, PIL.ImageFont, PIL.ImageDraw
import IPython.display as display
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
print("Tensorflow version " + tf.__version__)
# mnist = tf.keras.dataset.MNIST