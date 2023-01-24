

def main_loop(word):

    stages = ["               ",
              " ----------     ",
              " |        |     ",
              " |        0     ",
              " |      / | \   ",
              " |        |     ",
              " |       / \    ",
              "________________"]

    #start sets
    wrong = 0
    
    win = False
    letters = list(word.lower())

    board = ["__"] * len(word)

    print("Добро пожаловать в 'Висельницу' ")

    while ( wrong < len(stages) - 1):
        print("\n")
        message = "Введите букву: "
        char = input(message)
        char = char.lower()
        if (char not in letters):
            wrong += 1
            
        while char in letters:
            char_index = letters.index(char)
            letters[char_index] = "$"
            if (char_index == 0):
                board[char_index] = char.upper()
            else:
                board[char_index] = char
         
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "__" not in board:
              print("Вы победили! Слово было: ")
              print(" ".join(board))
              win = True
              break

    if (not win):
        print("Вы проиграли :( , Слово было: {}.".format(word.capitalize()))
        print("\n".join(stages))

    

