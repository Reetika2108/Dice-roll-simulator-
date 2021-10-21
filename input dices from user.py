import random
    
def generateRoll(num):#this is a comment
    diceAmount = []
    for i in range(int(num)):
        die = random.randrange(1, 7, 1)
        diceAmount.append(die)
        print('Die #' + str(i+1) + ' rolled a value of ' + str(die))    

x = 1
while(x != 0):
    print('Roll #' + str(x))
    numOfDice =  input('Enter the number of dice you want to roll: ')
    generateRoll(numOfDice)
    option = input('Enter 0 if you want to exit: ')
    if int(option) == 0:
        x = 0
    else:
        x += 1
print('Bye!')
