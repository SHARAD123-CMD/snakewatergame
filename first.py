import random
def game_win(user,computer):
    if user==computer:
        return None
    #snake vs water 
    if user=="s" and computer=="w":
        return True
    if user=="w" and computer=="s":
        return False

    #water vs gun
    if user=="w" and computer=="g":
        return True
    if user=="g" and computer=="w":
        return False
    # gun vs snake 
    if user=="g" and computer=="s":
            return True
    if user=="s" and computer=="g":
            return False
    
rand_no=random.randint(1,3)
print("computer's turn : water(w), snake(s), gun(g)")
if rand_no==1:
    computer= "s"
    
elif rand_no==2:
    computer= "w"
    
else:
    computer= "g"
    
user=input(" your turn : water(w), snake(s), gun(g)").lower() 
result= game_win(user, computer) 
print(f"\nyou chose :{user}")
print(f"\ncomputer chose :{computer}")
if result is None:
    print("its draw")
elif(result):
    print("you win")
else:
    print("you lose")