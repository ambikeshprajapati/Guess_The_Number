import random
def compare(guess):
    if guess==i:
        return None
    elif guess>i:
        return True
    else:
        return False
print("Welcome to guess a number game.")
print("Once started playing and want to quit then press 0")
print("Start guessing the number between 1-100.")
i=random.randint(1,100)
c=1
while(1!=0):
    g=int(input())
    if g==0 :
        print("You opted to exit the game.\nSee you next time.")
        break
    if compare(g)==True:
        print("Guess a smaller number")
        c +=1
    elif compare(g)==False:
        print("Guess a larger number")
        c+=1
    elif compare(g)==None:
        print(f"Yes, you guessed the correct number in {c} attempts.")
        with open("High_Score.txt","r") as f:
            hs=f.read()
            hs=int(hs)
            x=100-c
            if x>hs:
                with open("High_Score.txt","w")as f:
                    x=str(x)
                    hs=f.write(x)
        break
