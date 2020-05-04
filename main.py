import sys
from markov import Markov

def main():
    m = Markov(sys.argv[1])
    m.create_chain()
    m.generate_image('art.jpg')

if __name__ == '__main__':
    main()