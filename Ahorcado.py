import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']
WORDS = ['perejil', 
    'montante', 
    'termotanque', 
    'mondongo', 
    'choripan'
]

def random_word():
    indice = random.randint(0, len(WORDS) -1)
    return WORDS[indice]

def mostrar_tablero(palabra_escondida, intentos):
    print(IMAGES[intentos])
    print(' ')
    print(palabra_escondida)
    print('...')

def run():
    word = random_word()
    palabra_escondida = ['-'] * len(word)
    intentos = 0

    while True:
        mostrar_tablero(palabra_escondida, intentos)
        pido_letra = input('Escribe una letra ')

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == pido_letra:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            intentos += 1

            if intentos == 7:

                mostrar_tablero(palabra_escondida, intentos)
                print(' ')
                print('Perdiste cara de papa!! la palabra correcta era {}'.format(word))
                break

        else:
            for i in letter_indexes:
                palabra_escondida[i] = pido_letra
            letter_indexes = []

        try:
            palabra_escondida.index('-')
        except ValueError:
            print('')
            print('¡UFAAAAA! Ganaste ¬¬. felicidades...meh. La palabra es: {}'.format(word))
            break

    pass

if __name__ =='__main__':
    print('Bienvenido al Juego del ahorcado :D')
    run()
