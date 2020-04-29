import numpy as np
from PIL import Image

img = Image.open('example.jpg')
data = np.asarray(img)

chain = int(data.size * 0.2)

plain = [k for i in data for j in i for k in j ]

markov = {}

for pix in plain:
    pass