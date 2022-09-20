import random 

i = yv = cv = mt = 0  
choice = int(input('How many time you want to play this game '))
while(i < choice):
    lst = ['rock', 'paper', 'scissors'] 
    R = random.choice(lst)
    guess = input('\nenter your choice ').lower()
    print('\ncomputer guess',R)
    print('you guess',guess)

    if guess == 'rock' and R == 'scissors' or guess == 'scissors' and R == 'paper' or guess == 'paper' and R == 'rock' :
        print('You win!')
        yv = yv + 1
    elif guess == 'rock' and R == 'rock' or guess == 'paper' and R == 'paper' or guess == 'scissors' and R == 'scissors' :
        print('Match is tie')
        mt = mt + 1
    else:
        print('Computer is win')
        cv = cv + 1
        
    print('you play ',i+1,' times')

    i = i + 1

print('\n=============== Result ===============')
print('you win (', yv,') times')
print('Computer win (',cv,') times')
print('Match tie (',mt,') times')
if yv > cv:
    print('finally, You win!')
elif yv < cv:
    print('finally, Computer is win')
else:
    print('Match is tie')
