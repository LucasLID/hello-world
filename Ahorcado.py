import random
import os
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
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
WORDS=[
"papa",
"torta",
"cama",
"cocina"
]



def random_word(): 
    idx = random.randint(0,len(WORDS)-1)
    return WORDS[idx]

def display_board(hidden_word,tries):

    os.system('cls')  # windows
    
    print(IMAGES[tries])
    print("")
    print(hidden_word)
    print("--------------------------")
    

def run():
    letter_indexes=[]#//guarda los indices de las coincidencias entre la letra ingresada y la palabra a adivinar#
    word = random_word()
    hidden_word=["-"]* len(word)
    tries = 0
    
    while True:
        display_board(hidden_word,tries)
        current_letter = str(input("Escoge una letra: "))
        
        
        
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
                
        if len(letter_indexes) == 0:
            tries += 1
            
            if tries == 7:
                display_board(hidden_word, tries-1)
                print('')
                print("Perdiste, la palabra era: {}" .format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            letter_indexes = []
            
        try:
            hidden_word.index("-")
        except ValueError:
            display_board(hidden_word, tries)
            print('')
            print("Felicidades, ganaste. La palabra es : {}".format(word))
            break 
          
if __name__ == '__main__'   :
    
    print ("B I E N V E N I D O S  A  A H O R C A D O")
    
    run()
    print("")
    input("Presione Cualquier tecla para salir") 