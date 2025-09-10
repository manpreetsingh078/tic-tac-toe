def sum(a,b,c):
    return a+b+c

def printboard(xstate,zstate):
    zero = 'x' if xstate[0] else ('o' if zstate[0] else 0)
    one = 'x' if xstate[1] else ('o' if zstate[1] else 1)
    two = 'x' if xstate[2] else ('o' if zstate[2] else 2)
    three = 'x' if xstate[3] else ('o' if zstate[3] else 3)
    fourth = 'x' if xstate[4] else ('o' if zstate[4] else 4)
    fifth = 'x' if xstate[5] else ('o' if zstate[5] else 5)
    sixth = 'x' if xstate[6] else ('o' if zstate[6] else 6)
    seventh = 'x' if xstate[7] else ('o' if zstate[7] else 7)
    eighth = 'x' if xstate[8] else ('o' if zstate[8] else 8)

    print(f"{zero}  | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {fourth} | {fifth} ")
    print(f"---|---|---")
    print(f" {sixth} | {seventh} | {eighth} ")

def checkwin(xstate,zstate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("X won the match")
            return 1
        if(sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):
            print("O won the match")
            return 0
    return -1   

if __name__ =="__main__":
    xstate=[0,0,0,0,0,0,0,0,0]
    zstate=[0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for x and 0 for o
    print("welcome to tic tac toe")
    while(True):
        printboard(xstate,zstate)
        if (turn==1):
            print("it's X turn")
            value=int(input("enter the value: "))
            xstate[value]=1
        else:
            print("it's O turn")
            value=int(input("enter the value: "))
            zstate[value]=1
        cwin=checkwin(xstate,zstate)
        if(cwin != -1):
            print("match over")
            break
        turn=1-turn

