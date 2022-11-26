import random 
import os

def get_word():
    words_list=[]
    with open("./words.txt") as txt: 
        for word in txt:    
            words_list.append(word)

    word = random.choice(words_list)
    return word.upper()

def display_game_name():
    #print("\t\t-------------")
    print("\t========== HANGMAN ==========")
    #print("\t\t-------------")

def play(word):
    characters = "_" * (len(word)-1)
    flag = False
    predicted_letters =[]
    predicted_words = []
    prediction_number = 6
    display_game_name()
    print(draw_hangman(prediction_number))
    print(characters)

    while not flag and prediction_number > 0:
        guess = input("Guess a word or letter: ").upper()
        display_game_name()
        if len(guess) == 1 and guess.isalpha():
            if guess in word:
                print("Good job,", guess, "is in the word!")
                predicted_letters.append(guess)
                word_as_list = list(characters)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                characters = "".join(word_as_list)
                if "_" not in characters:
                    flag = True
            elif guess in predicted_letters:
                print("You already guessed the letter", guess)
            else:
                print(guess, "is not in the word.")
                prediction_number -= 1
                predicted_letters.append(guess)


        elif len(guess) == len(word) and guess.isalpha():
            if guess != word:
                print(guess, "is not the word.")
                prediction_number -= 1
                predicted_words.append(guess)
            else:
                flag = True
                characters = word
        else:
            print("Wrong Systax.")
        print(draw_hangman(prediction_number))
        print(characters)
        print("\n")
    if flag:
        print("CONGRATULATIONS !! YOU WIN !! YOU FOUND THE RIGHT WORD")
    else:
        print("The word was " + word)

        
def draw_hangman(prediction_number):
    stages = [  
                """

                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                1 chance left
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
               
                """
                2 chance left
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                
                """
                 3 chance left
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
               
                """

                4 chance left
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                 
                5 chance left                 
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[prediction_number]    

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()