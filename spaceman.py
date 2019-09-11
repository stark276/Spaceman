import random



def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter in letters_guessed:
            continue
        else:
            return False
    return True   # Underdtand
    #pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in
     the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, 
        the string should contain the letter at the correct position.  For letters in the word that the
         user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string 
    # that shows the letters that have been guessed correctly so far 
    # that are saved in letters_guessed and underscores for the letters 
    # that have not been guessed yet
    sec_word = ""

    for letter in secret_word:
        if letter in letters_guessed:
             sec_word += letter
        else:
            sec_word += "*"
    return sec_word        ###UNDERSTAND
    
    #pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word #
    if guess in secret_word:
        return True
    else:
        return False

    # pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed = []
    tries = 7
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    #2TODO: Ask the player to guess one letter per round and check that it is only one letter
    #1TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman")
    print(f"The secret word holds: {len(secret_word)} letters")
    print("You have 7 attempts left, please enter your letter ")
    while tries > 0:

        print("-------------------------")
        print(secret_word)
   
        guess = input("Enter your letter: ")
        
        #print(guess)
        
        while len(guess) != 1:
            guess = input("Please enter only one letter. Try again: ")
       
        while guess.isdigit() == True:
            guess = input("Please enter only a letter. Try again: ")
       
        while guess in letters_guessed:
            guess = input("You have already tried this letter, Try again: ")

        letters_guessed.append(guess)
        print(get_guessed_word(secret_word, letters_guessed))

        if is_guess_in_word(guess, secret_word) == True:
            print("Correct, Bingo!")
        else:   
            tries -= 1
            print("Incorrect") 

        print("Letters guessed already: ", letters_guessed)

        alphabet.remove(guess)
         
        print("Letters remaining:","".join(alphabet))
        print("Remaining tries:", tries)
        if is_word_guessed(secret_word, letters_guessed) == True:
            return print("Congratulations!You just won 10000000$!")
        if tries == 0:
            print("You just lost 1000000$, try again!")
        



    
    #3TODO: Check if the guessed letter is in the secret or not and give the player feedback
    #4TODO: show the guessed word so far
    #5TODO: check if the game has been won or lost
 
#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
answer = input('Would you like to play again Y/N: ')

while answer == 'Y' or answer == 'y':
    secret_word = load_word()
    spaceman(secret_word)
    answer = input('Would you like to play again Y/N: ')