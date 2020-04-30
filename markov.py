import numpy as np
import random as rnd

class Markov():

    def __init__(self, img, per):
        self.img = img
        self.per = per
        self.chain = {}

    def create_chain(self):
        plain = [ k for i in self.img for j in i for k in j ]

        for i in range(0, len(plain), 3):
            pix = Markov.pix_str(i, plain)
            
            if not pix in self.chain:
                self.chain[pix] = []
            
            self.chain[pix].append(Markov.pix_str(i+3, plain))

    def generate_image(self):
        pass

    @staticmethod
    def pix_str(index, pixels):
        p = map(lambda x: str(x), pixels[index:index+3])
        return ','.join(p)

    @staticmethod
    def pix_arr(pix):
        p = pix.split(',')
        p = map(lambda  x: int(x), pix)
        return list(p)