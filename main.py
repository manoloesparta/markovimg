import numpy as np
from markov import Markov
from PIL import Image

def main():
    img = Image.open('we.jpg')
    data = np.asarray(img)

    c = Markov(data, 3)
    c.create_chain()
    gen = c.generate_image()
    x = Image.fromarray(gen, mode='RGB')
    x.save('art.jpg')
    
if __name__ == "__main__":
    main()