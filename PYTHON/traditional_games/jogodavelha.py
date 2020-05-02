'''Crie um tabuleiro de jogo da velha, usando uma matrizes de caracteres 3x3, onde o usuário pede o número da linha (1 até 3)
 e o da coluna (1 até 3). A cada vez que o usuário entrar com esses dados, colocar um 'X' ou 'O' no local selecionado.'''

player1 = input("Player 1, choose if you are X ou O: ")

if player1.upper() == 'X':
    player1 = 'X'
    player2 = 'O'
    print("Player 2, as Player 1 choosed %s, you will be %s" % ('X', 'O'))
elif player1.upper() == 'O':
    player1 = 'O'
    player2 = 'X'
    print("Player 2, as Player 1 choosed %s, you will be %s" % ('O', 'X'))
else:
    print("You only can choose X or O, try again!")
    player1 = input("Player 1, choose if you are X ou O: ")

print("Let's get it started!!!")

board = [['__', '__', '__'], ['__', '__', '__'], ['__', '__', '__']]


def printboard():
    for i in range(len(board)):
        print(board[i])
printboard()

def choice(player):
    playeri = int(input("choose the line that you want to mark: "))
    playerj = int(input("choose the column that you want to mark:"))

    if board[playeri - 1][playerj - 1] == '__':
        del board[playeri - 1][playerj - 1]
        board[playeri - 1].insert((playerj - 1), player)
        print("Next player, please")
        printboard()
        return True
    else:
        print("That place already has a mark! choose another one!")
        return False

def play():
    while result() != 'X' or result() != 'O':
        if result() == 'X':
            if player1 == 'X':
                print("!*!*!*! Player 1 Wins !*!*!*!")
                break
            else:
                print("!*!*!*! Player 2 Wins !*!*!*!")
                break

        if result() == 'O':
            if player1 == 'O':
                print("!*!*!*! Player 1 Wins !*!*!*!")
                break
            else:
                print("!*!*!*! Player 2 Wins !*!*!*!")
                break
        for i in range(1, 6):
            print("Round #%s" % i)
            print("==== Player 1, it's your turn ====")
            if choice(player1) == False:
                choice(player1)
            result()
            if result() == 'X' or result() == 'O':
                break
            if i > 4:
                print("^.^.^.^ DRAW! ^.^.^.^")
            else:
                print("==== Player 2, it's your turn ====")
                if choice(player2) == False:
                    choice(player2)
                result()
                if result() == 'X' or result() == 'O':
                    break

def result():
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or \
            board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' or \
            board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' or \
            board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or \
            board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or \
            board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X' or \
            board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or \
            board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
        winner = 'X'
        return winner

    if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O' or \
            board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O' or \
            board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O' or \
            board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' or \
            board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O' or \
            board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O' or \
            board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or \
            board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
        winner = 'O'

        return winner


play()

