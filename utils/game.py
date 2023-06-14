class Hangman:
    def __init__(self):
        self.possible_words = ['BeCode']
        self.word_to_find = self.possible.words
        self.lives = 5
        self.correctly_guessed_letters = [" _ "] * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
 
    
    def play(self):
        self.user_input = input("Add ONLY letter: ")
        if self.user_input.isalpha() & len(self.user_input) == 1:
            for index, letter in enumerate(self.word_to_find):
                if letter == self.user_input:
                    self.correctly_guessed_letters[index] = letter
                else:
                    self.wrongly_guessed_letters.append(letter)
                    self.lives -= 1
                    self.error_count += 1  

                self.turn_count += 1 
        else:
            print("Your input is not a letter")

    def start_game(self):
        print("Welcome to Hangman!😎")
        while True:
            self.play()
            if "_" not in self.correctly_guessed_letters:

    def game_over(self):
        print("geme over...")

            


            


        


        

