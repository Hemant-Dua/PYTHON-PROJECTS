def printboard(X,O):
    a='X' if X[0]==1 else("O" if O[0]==1 else 0)
    b='X' if X[1]==1 else("O" if O[1]==1 else 1)
    c='X' if X[2]==1 else("O" if O[2]==1 else 2)
    d='X' if X[3]==1 else("O" if O[3]==1 else 3)
    e='X' if X[4]==1 else("O" if O[4]==1 else 4)
    f='X' if X[5]==1 else("O" if O[5]==1 else 5)
    g='X' if X[6]==1 else("O" if O[6]==1 else 6)
    h='X' if X[7]==1 else("O" if O[7]==1 else 7)
    i='X' if X[8]==1 else("O" if O[8]==1 else 8)
    
    print(f" {a} | {b} | {c} ")
    print(f"---|---|---")
    print(f" {d} | {e} | {f} ")
    print(f"---|---|---")
    print(f" {g} | {h} | {i} ")

def checkwin(X,O):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (X[win[0]]+X[win[1]]+X[win[2]])==3:
            printboard(X,O)
            print("X Wins...")
            return 1
        
        elif (O[win[0]]+O[win[1]]+O[win[2]])==3:
            printboard(X,O)
            print("O Wins...")
            return 0

    return -1

if __name__ == "__main__":

    print("------------------TIC TAC TOE.EXE--------------------")

    X=[0,0,0,0,0,0,0,0,0]
    O=[0,0,0,0,0,0,0,0,0]

    # 1 for X and 0 for O
    turn=1

    while True:
        
        printboard(X,O)

        if (turn == 1):    
            print("X's Turn")
            value=int(input("Please Enter a value..."))
            X[value]=1
            turn=0
            
        else:
            print("O's Turn")
            value=int(input("Please Enter a value..."))
            O[value]=1
            turn=1
        
        check = checkwin(X,O)
        if check !=-1:
            print("Match Over...")
            break