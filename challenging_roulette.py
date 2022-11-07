import random
import sys
import re

colors = "red","black"
minimum_amount = 59.99
random_number = random.randint(0,30) 
random_color = random.choice(colors)
random_dices_numbers = random.randint(1,6)      
cuantity_numbers = [] 
cuantity_colors = []



def main(bettor_money,win):
    if win == "one number roulette":
        return bettor_money *12
    if win == "many numbers roulette":
        return bettor_money *6
    if win == "number dices":
        return bettor_money *5

def numbers(roulette_number):
    if re.search(r'([A-Za-z]|\s|\ñ)', roulette_number):
        raise ValueError("This is not a number")
    
    elif roulette_number == "":
        raise ValueError("There's nothing here")
        
    elif re.search(r'^([0-9]|1[0-9]|2[0-9]|30)$',roulette_number):
       cuantity_numbers.append(int(roulette_number))
    
    elif re.search(r'^(([0-9]|1[0-9]|2[0-9]|30)\,){1,4}([0-9]|1[0-9]|2[0-9]|30)$',roulette_number):
        separator_numbers = re.split(r',',roulette_number)
        for element in separator_numbers:
            cuantity_numbers.append(int(element))
         
    else:
        raise ValueError("Is only number between 0 and 30 and is a number or 5 numbers")


def color(roulette_color):
    if re.search(r'\d|\W',roulette_color) and len(roulette_color) != 1:
        raise ValueError("Is only a color")
    
    elif roulette_color not in colors:
        raise ValueError("This color is not available")
    
    else:
        cuantity_colors.append(roulette_color)


def dices(number_dices):
    if re.search(r'^[1-6]$', number_dices) and len(number_dices) == 1: 
        return int(number_dices)
    else:
        raise ValueError("Is a number between 1 and 6")


try:
    print("\U0001f38a \U0001f3b2 ¡Welcome to the challenging roulette! \U0001f3b2 \U0001f38a")
    amount_bettor = float(input("Please, type your amount \U0001f4b2"))
    if amount_bettor >= minimum_amount:
            print("¡Choose a number, one number for three turns or two to five numbers for one turn!")
    else:
        sys.exit("Sorry, you don't have enough money \U0001f625")
except ValueError:
    sys.exit("That's not possible")

numbers(input('Type your number or numbers with "," between 0 and 30: '))
color(input("Type your colors: "))

if len(cuantity_numbers) == 1:
        if random_color and random_number in cuantity_numbers and cuantity_colors:
            print(f'Congratulations, you win \U0001f4b2{main(amount_bettor,"one number roulette")} dollars')
            
        else:
            sys.exit(f"Sorry you lose, the number isn't the right one, the right number is {random_number} {random_color} \U0001f625")

if len(cuantity_numbers) >= 2 and len(cuantity_numbers) <= 5:
        if random_color and random_number in cuantity_numbers and cuantity_colors:
            print(f'Congratulations, you win \U0001f4b2 {main(amount_bettor,"many numbers roulette")} dollars')
        else:
            sys.exit(f"Sorry you lose, the number isn't the right one, the right number is {random_number} {random_color} \U0001f625")


confirmation = input("You have the chance to bet with dices, do you wish to follow or retirate with the earned money?\U0001f3b2\U0001f3b2 ")

if re.search(r'^(yes|Yes)$',confirmation):
    
    if dices(input("Type the dices number: ")) == random_dices_numbers:
        print(f'Congratulations you win \U0001f4b2{main(amount_bettor,"number dices")} dollars')
        
        if len(cuantity_numbers) == 1:
            print(f'Now you have \U0001f4b2{main(amount_bettor,"one number roulette") + main(amount_bettor,"number dices")} dollars, Congratulations')
        
        elif len(cuantity_numbers) >= 2 and len(cuantity_numbers) <= 5:
             print(f'Now you have \U0001f4b2{main(amount_bettor,"many numbers roulette") + main(amount_bettor,"number dices")} dollars, Congratulations')

    else:
        sys.exit("Sorry, you lose everything, better luck next time \U0001f625")

elif re.search(r'^(no|No)$', confirmation):
    
    if len(cuantity_numbers) == 1:
        sys.exit(f'Thank you for playing this amazing roulette, you retirate with you earned money \U0001f4b2{main(amount_bettor,"one number roulette")} dollars')

    elif len(cuantity_numbers) >= 2 and len(cuantity_numbers) <= 5:
        sys.exit(f'Thank you for playing this amazing roulette, you retirate with you earned money \U0001f4b2{main(amount_bettor,"many numbers roulette")} dollars')

else:
    raise ValueError("Is only yes or no")
