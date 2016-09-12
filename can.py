
from random import randint

class game():
    def __init__(self):
        self.game = [[" "," "," "], [" "," "," "], [" "," "," "]]
        self.players = ["X", "O"]

def print_game(gms):
    for x in range(0, 5):
        if (x % 2 != 0):
            print("------")
        else:
            for y in range(0, 5):
                if (y % 2 != 0):
                    print("|", end="")
                else:
                    print("".join(gms.game[int(x / 2)][int(y / 2)]), end="")
                if y == 4:
                    print()

def play_human(game, player):
    option = input("select position AxB: ")
    #print("\033[F", end="")
    string = option.split("x")
    if (not string[0].isdigit() or not string[1].isdigit()):
       # print("Please, enter a position in an AxB form")
        clear_game()
        print_game(game)
        play_human(game, player)
        #print("\033[F", end="")
        return
    Y = int(string[1])
    X = int(string[0])
    if (Y > 2 or X > 2 and (Y < 0 or X < 0)):
      #  print("Please, enter a number less than 2 and bigger than 0")
        clear_game()
        print_game(game)
        play_human(game, player)
        #print("\033[F", end="")
        return
    if (game.game[X][Y] != " "):
       # print("That position is ocupated, but you can choose another, WooooW")
        clear_game()
        print_game(game)
        play_human(game, player)
        #print("\033[F", end="")
        return
    game.game[X][Y] = game.players[player]
    return

def play_machine(game, machine):
    
    
    #2 on place for the win
        
    #horizontal
    for x in range(0, 2):
        if(game.game[x][0] == game.game[x][1] and game.game[x][0] == game.players[machine]):
            if (game.game[x][2] == " "):
                game.game[x][2] = game.players[machine]
                return
        if(game.game[x][1] == game.game[x][2] and game.game[x][1] == game.players[machine]):
            if (game.game[x][0] == " "):
                game.game[x][0] = game.players[machine]
                return
        if(game.game[x][0] == game.game[x][2] and game.game[x][0] == game.players[machine]):
            if (game.game[x][1] == " "):
                game.game[x][1] = game.players[machine]
                return
    #vertical
    for y in range(0, 2):
        if(game.game[0][y] == game.game[1][y] and game.game[0][y] == game.players[machine]):
            if (game.game[2][y] == " "):
                game.game[2][y] = game.players[machine]
                return
        if(game.game[1][y] == game.game[2][y] and game.game[1][y] == game.players[machine]):
            if (game.game[0][y] == " "):
                game.game[0][y] = game.players[machine]
                return
        if(game.game[0][y] == game.game[2][y] and game.game[0][y] == game.players[machine]):
            if (game.game[1][y] == " "):
                game.game[1][y] = game.players[machine]
                return
    
    #diagonal
    if(game.game[0][0] == game.game[1][1] and game.game[0][0] == game.players[machine]):
            if (game.game[2][2] == " "):
                game.game[2][2] = game.players[machine]
                return
    if(game.game[1][1] == game.game[2][2] and game.game[1][1] == game.players[machine]):
        if (game.game[0][0] == " "):
            game.game[0][0] = game.players[machine]
            return
    if(game.game[0][0] == game.game[2][2] and game.game[0][0] == game.players[machine]):
            if (game.game[1][1] == " "):
                game.game[1][1] = game.players[machine]
                return
    
    #diagonal inverse
    if(game.game[0][2] == game.game[1][1] and game.game[0][2] == game.players[machine]):
        if (game.game[2][0] == " "):
            game.game[2][0] = game.players[machine]
            return
    if(game.game[1][1] == game.game[2][0] and game.game[1][1] == game.players[machine]):
        if (game.game[0][2] == " "):
            game.game[0][2] = game.players[machine]
            return
    if(game.game[0][2] == game.game[2][0] and game.game[0][2] == game.players[machine]):
        if (game.game[1][1] == " "):
            game.game[1][1] = game.players[machine]
            return
    
    
    #2 on place
        
    #horizontal
    for x in range(0, 2):
        if(game.game[x][0] == game.game[x][1] and game.game[x][0] != " "):
            if (game.game[x][2] == " "):
                game.game[x][2] = game.players[machine]
                return
        if(game.game[x][1] == game.game[x][2] and game.game[x][1] != " "):
            if (game.game[x][0] == " "):
                game.game[x][0] = game.players[machine]
                return
        if(game.game[x][0] == game.game[x][2] and game.game[x][0] != " "):
            if (game.game[x][1] == " "):
                game.game[x][1] = game.players[machine]
                return
    #vertical
    for y in range(0, 2):
        if(game.game[0][y] == game.game[1][y] and game.game[0][y] != " "):
            if (game.game[2][y] == " "):
                game.game[2][y] = game.players[machine]
                return
        if(game.game[1][y] == game.game[2][y] and game.game[1][y] != " "):
            if (game.game[0][y] == " "):
                game.game[0][y] = game.players[machine]
                return
        if(game.game[0][y] == game.game[2][y] and game.game[0][y] != " "):
            if (game.game[1][y] == " "):
                game.game[1][y] = game.players[machine]
                return
    
    #diagonal
    if(game.game[0][0] == game.game[1][1] and game.game[0][0] != " "):
            if (game.game[2][2] == " "):
                game.game[2][2] = game.players[machine]
                return
    if(game.game[1][1] == game.game[2][2] and game.game[1][1] != " "):
        if (game.game[0][0] == " "):
            game.game[0][0] = game.players[machine]
            return
    if(game.game[0][0] == game.game[2][2] and game.game[0][0] != " "):
            if (game.game[1][1] == " "):
                game.game[1][1] = game.players[machine]
                return
    
    #diagonal inverse
    if(game.game[0][2] == game.game[1][1] and game.game[0][2] != " "):
        if (game.game[2][0] == " "):
            game.game[2][0] = game.players[machine]
            return
    if(game.game[1][1] == game.game[2][0] and game.game[1][1] != " "):
        if (game.game[0][2] == " "):
            game.game[0][2] = game.players[machine]
            return
    if(game.game[0][2] == game.game[2][0] and game.game[0][2] != " "):
        if (game.game[1][1] == " "):
            game.game[1][1] = game.players[machine]
            return
                
                
    #1 on place
                
    #horizontal
    for x in range(0, 2):
        if (game.game[x][0] == game.players[machine]):
            if (game.game[x][1] == " "):
                game.game[x][1] = game.players[machine]
                return
        if (game.game[x][1] == game.players[machine]):
            if (game.game[x][2] == " "):
                game.game[x][2] = game.players[machine]
                return
        if (game.game[x][2] == game.players[machine]):
            if (game.game[x][1] == " "):
                game.game[x][1] = game.players[machine]
                return
        if (game.game[x][1] == game.players[machine]):
            if (game.game[x][0] == " "):
                game.game[x][0] = game.players[machine]
                return
        
    #vertical
    for y in range(0, 2):
        if (game.game[0][y] == game.players[machine]):
            if (game.game[1][y] == " "):
                game.game[1][y] = game.players[machine]
                return
        if (game.game[1][y] == game.players[machine]):
            if (game.game[2][y] == " "):
                game.game[2][y] = game.players[machine]
                return
        if (game.game[1][y] == game.players[machine]):
            if (game.game[0][y] == " "):
                game.game[0][y] = game.players[machine]
                return
        if (game.game[2][y] == game.players[machine]):
            if (game.game[1][y] == " "):
                game.game[1][y] = game.players[machine]
                return
                
    #diagonal
    if (game.game[0][0] == game.players[machine]):
        if (game.game[1][1] == " "):
            game.game[1][1] = game.players[machine]
            return
    if (game.game[1][1] == game.players[machine]):
        if (game.game[2][2] == " "):
            game.game[2][2] = game.players[machine]
            return
    if (game.game[1][1] == game.players[machine]):
        if (game.game[0][0] == " "):
            game.game[0][0] = game.players[machine]
            return
    if (game.game[2][2] == game.players[machine]):
        if (game.game[1][1] == " "):
            game.game[1][1] = game.players[machine]
            return
    
    #diagonal inverse
    if (game.game[0][2] == game.players[machine]):
        if (game.game[1][1] == " "):
            game.game[1][1] = game.players[machine]
            return
    if (game.game[1][1] == game.players[machine]):
        if (game.game[2][0] == " "):
            game.game[2][0] = game.players[machine]
            return
    if (game.game[1][1] == game.players[machine]):
        if (game.game[0][2] == " "):
            game.game[0][2] = game.players[machine]
            return
    if (game.game[2][0] == game.players[machine]):
        if (game.game[1][1] == " "):
            game.game[1][1] = game.players[machine]
            return
            
            
    #0 on place
    while(1):
        x = randint(0,2)
        y = randint(0,2)
        if (game.game[x][y] == " "):
            game.game[x][y] = game.players[machine]
            return 
        
    
def check_winner(game):
    for x in range(0, 2):
        if (game.game[x][0] != " "):
            if game.game[x][0] == game.game[x][1]:
                if game.game[x][1] == game.game[x][2]:
                    #clear_game()
                    #print_game(game)
                    print("\rWinner is " + game.game[x][0])
                    return True
    for y in range(0, 2):
        if (game.game[0][y] != " "):
            if game.game[0][y] == game.game[1][y]:
                if game.game[1][y] == game.game[2][y]:
                    #clear_game() 
                    #print_game(game) 
                    print("\rWinner is " + game.game[0][y])
                    return True
                    
    if (game.game[0][0] == game.game[1][1] and game.game[1][1] == game.game[2][2] and game.game[0][0] != " "):
        #clear_game()
        #print_game(game)
        print("\rWinner is " + game.game[0][0])
        return True                 
    if (game.game[0][2] == game.game[1][1] and game.game[1][1] == game.game[2][0] and game.game[0][2] != " "):
        #clear_game()
        #print_game(game)
        print("\rWinner is " + game.game[0][2])
        return True


def clear_game():
    for x in range(0, 6):
        print("\033[F", end="")

game1 = game()
print_game(game1)
for x in range(0, 9):
    if (check_winner(game1)):
        break
    play_human(game1, 0)
    play_machine(game1, 1)
    clear_game()
    print_game(game1)
        
        
        
