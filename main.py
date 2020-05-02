import numpy as np
from markov import Markov
from PIL import Image

def main():
    c = Markov('we.jpg')
    c.create_chain()
    gen = c.generate_image()
    x = Image.fromarray(gen, mode='RGB')
    x.save('art.jpg')
    
if __name__ == "__main__":
    main()