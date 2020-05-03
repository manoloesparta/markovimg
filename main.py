import numpy as np
from markov import Markov
from PIL import Image

def main():
    c = Markov('we.jpg')
    c.create_chain()
    c.generate_image("art.jpg")
    
if __name__ == "__main__":
    main()