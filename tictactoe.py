
def printboard(board):
    print(f'''|{board[0]}|{board[1]}|{board[2]}|
|{board[3]}|{board[4]}|{board[5]}|
|{board[6]}|{board[7]}|{board[8]}|''')

def countempty(board):
    emptylist = []
    for i in board:
        if i == ' ':
            emptylist.append(i)
    return emptylist

def insertpiece(board, location, symbol):
    board[location]=symbol
    return board

def playermove(board):
    location = int(input('Where do you want to place your symbol?'))-1
    if board[location] == ' ':
        insertpiece(board, location, 'X')
    else:
        print('That\'s not a valid move! Try again!')
        playermove(board)

def computermove(board):
    for i in [8,7,6,5,4,3,2,1,0]:
        if board[i] == ' ':
            insertpiece(board, i, 'O')
            break

def windetected(symbol, board):
    if board[0] == board[1] and board[1] == board[2] and board[0] == symbol: return True
    elif board[3] == board[4] and board[4] == board[5] and board[3] == symbol: return True
    elif board[6] == board[7] and board[7] == board[8] and board[6] == symbol: return True
    elif board[0] == board[4] and board[4] == board[8] and board[0] == symbol: return True
    elif board[2] == board[4] and board[4] == board[6] and board[2] == symbol: return True
    elif board[0] == board[3] and board[3] == board[6] and board[0] == symbol: return True
    elif board[1] == board[4] and board[4] == board[7] and board[1] == symbol: return True
    elif board[2] == board[5] and board[5] == board[8] and board[2] == symbol: return True
    else: return False

def main():
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    goes_first=input('Would you like to go first? y/n').lower()
    if goes_first=='n':
        while len(countempty(board)) > 0:
            computermove(board)
            if windetected('O', board):
                print('Computer wins!')
                main()
            printboard(board)
            playermove(board)
            printboard(board)
            if windetected('X', board): 
                print('You win!')
                main()
                goes_first-' '
            else:
                continue
        main()
    elif goes_first=='y':
        while len(countempty(board)) > 0:
            playermove(board)
            printboard
            if windetected('X', board):
                print('You win!')
                main()
            computermove(board)
            
            if windetected('O', board): 
                print('Computer wins!')
                main()
                goes_first=' '
            else:
                continue
        main()
    else:
        pass

if __name__ == '__main__':
    main()
