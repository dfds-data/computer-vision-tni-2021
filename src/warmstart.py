"""
Try predicting on a sample image.

Used in the Dockerfile to make sure all relevant binary blobs are already downloaded before running
the app.
"""

from PIL import Image

from src.demo import detect_age_gender

img = Image.open("imgs/itamar.jpg")
detect_age_gender(img)
