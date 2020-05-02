import numpy as np
import random as rnd
from PIL import Image


class Markov():

    def __init__(self, img):
        tmp = Image.open(img)
        data = np.asarray(tmp)

        self.img = data
        self.plain = [ k for i in self.img for j in i for k in j ]
        self.chain = {}

    def create_chain(self):
        for i in range(0, len(self.plain), 3):
            pix = Markov.pix_str(self.plain[i:i+3])
            
            if not pix in self.chain:
                self.chain[pix] = []
            
            self.chain[pix].append(Markov.pix_str(self.plain[i+3:i+6]))

    def generate_image(self):
        start = rnd.choice(list(self.chain.keys()))
        result = []

        for _ in range(500 * 500):
            possible = self.chain[start]
            chosen = rnd.choice(possible)

            if chosen == '':
                chosen = rnd.choice(list(self.chain.keys()))
            
            start = chosen
            result.append(Markov.pix_arr(start))

        return self._to_matrix(result)

    def _to_matrix(self, arr):
        matrix = []
        for i in range(500):
            row = []
            for j in range(500):
                row.append(arr[(i * 500)+j])
            matrix.append(row)
        return np.array(matrix, dtype=np.uint8)

    @staticmethod
    def pix_str(pixels):
        p = map(lambda x: str(x), pixels)
        return ','.join(p)

    @staticmethod
    def pix_arr(pix):
        p = pix.split(',')
        p = map(lambda  x: int(x), p)
        return list(p)