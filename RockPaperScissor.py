import random
def play():
    player1=str(input("r for rock,p for paper,s for scissors:")).lower()
    choose=["r","p","s"]
    player2=random.choice(choose)
    print(f'your choice:{player1}<=>opponent{player2}')
    if(player1==player2):
        print("game is in tie!")
    elif((player1=="r" and player2=="s") or (player1=="p" and player2=="r") or (player1=="s" and player2=="r")):
        print("you won the game")
    else:
        print("good try")     
play()               