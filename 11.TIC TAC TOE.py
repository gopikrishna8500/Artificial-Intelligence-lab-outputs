def sum(a,b,c):
    return a+b+c
def printBoard(xState , zState):
    zero =  'X' if xState[0] else('@' if zState[0] else 0 )
    one =  'X' if xState[1] else('@' if zState[1] else 1 )
    two =  'X' if xState[2] else('@' if zState[2] else 2 )
    three =  'X' if xState[3] else('@' if zState[3] else 3 )
    four =  'X' if xState[4] else('@' if zState[4] else 4 )
    five =  'X' if xState[5] else('@' if zState[5] else 5 )
    six =  'X' if xState[6] else('@' if zState[6] else 6 )
    seven =  'X' if xState[7] else('@' if zState[7] else 7 )
    eight =  'X' if xState[8] else('@' if zState[8] else 8 )
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
def checkWin(xState,zState) : 
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins :
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3) :
            print("X won the game")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3) :
            print("O won the game.")
            return 0
    return -1
if __name__ == "__main__" : 
    total_turns = 9
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    turn = 1 # 1 for X and 0 for O
    print("Welcome to TIC-TAC-TOE")
    while(True) : 
        printBoard(xState, zState)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value : "))
            xState[value] = 1
        else :
            print("O's Chance")
            value = int(input("Please enter a value : "))
            zState[value] = 1
        total_turns = total_turns - 1
        if(checkWin(xState, zState) != -1 or total_turns == 0 ):
            print("GAME OVER")
            printBoard(xState, zState)
            break
        turn = 1 -  turn
