import random

class Hangman:
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = random.choice(self.possible_words).lower()  # Select a random word from the list
        self.correctly_guessed_letters = list("_" * len(self.word_to_find))  # Create a list to store correctly guessed letters
        self.wrongly_guessed_letters = []  # Create a list to store wrongly guessed letters
        self.lives = 5  # Set the number of lives
        self.turn_count = 0  # Initialize the turn count
        self.error_count = 0  # Initialize the error count

    def play(self):
        while True:
            self.user_input = input("Add ONLY letter (type 'quit' to exit): ").lower()  # Get user input
            if self.user_input == 'quit':  # Check if the user wants to exit
                self.quit_game()
                break
            if len(self.user_input) == 1 and self.user_input.isalpha():  # Check if the user input is a single letter
                break
            else:
                print("Invalid input! Please enter a single letter.")

        if self.user_input in self.word_to_find:  # Check if the user input is in the word
            for i, char in enumerate(self.word_to_find):  # Iterate over the word
                if char == self.user_input:  # If the character matches the user input
                    self.correctly_guessed_letters[i] = self.user_input  # Update the correctly guessed letters list
        else:
            if self.user_input not in self.wrongly_guessed_letters:  # If the user input is not already in the wrongly guessed letters list
                self.wrongly_guessed_letters.append(self.user_input)  # Add the user input to the wrongly guessed letters list
                self.lives -= 1  # Decrease the number of lives
                self.error_count += 1  # Increase the error count

        self.turn_count += 1  # Increase the turn count

    def start_game(self):
        print(f"Welcome to Hangman game☠️! Word to find has {len(self.word_to_find)} letters")
        while True:
            self.play()  # Call the play() method to get user input and update game state

            if self.user_input == 'quit':  # Check if the user wants to quit
                break

            if "_" not in self.correctly_guessed_letters:  # If there are no more underscores in the correctly guessed letters list
                self.well_played()  # Call the well_played() method
                break

            if self.lives == 0:  # If the number of lives reaches 0
                self.game_over()  # Call the game_over() method
                break

            # Display game information to the user
            print(f"Your correctly guessed letters: {' '.join(self.correctly_guessed_letters)}")
            print(f"Your bad guessed letters: {self.wrongly_guessed_letters}")
            print(f"Your lives: {self.lives}")
            print(f"Your error count: {self.error_count}")
            print(f"Your turn count: {self.turn_count}")

    def game_over(self):
        print("Game over... The word was:", self.word_to_find)

    def well_played(self):
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")

    def quit_game(self): # you didn't mention this method in the game mission but i found it useful😉
        print("Quitting the game...")
