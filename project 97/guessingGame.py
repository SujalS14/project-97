import random
number=random.randint(1,9)
chances = 5
print("Guess a Number from 1 to 9:")

while chances < 5:
    guess = int(input("Your guess:"))

    if chances <= 5 and guess == number:
        print ("Congratulations you won!!!")
        break
    
    if not chances < 5 and guess!= number:
        print("YOU LOSE!!! The number was", number)
