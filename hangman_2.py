
def start_screen(color):
    pass

def get_puzzle():
    return "zooweemama"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    return input("guess a letter")

def display_board(solved):
    return ("_"*len(puzzle))

def show_result():
    pass

def play_again():
    while True:
        again=input("do you wanna play again? (y/n)")
        if again == y:
            return True
        elif again == n:
            return False
        else:
            print("i don't understand. please say y or n")
    
def play():
    puzzle = get_puzzle()
    solved = get_solved(puzzle, guesses)
    letter = get_guess()

    guesses += letter
    
    
    
play()
