import numpy as np
from markov import Markov
from PIL import Image

def main():
    img = Image.open('example.jpg')
    data = np.asarray(img)

    c = Markov(data, 0.2)
    c.create_chain()
    
    print(c.chain)

if __name__ == "__main__":
    main()