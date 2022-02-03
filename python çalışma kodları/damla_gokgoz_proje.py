import random
import time


while True:    
    first_heros_name = input("----- First Hero ----- \n Please type your hero's name: ")
    if len(first_heros_name) > 1:
        print ("First hero's name is", first_heros_name.capitalize())
        break
    else:
        print ("Length of hero's name must be longer than 1 character.")

while True:    
    second_heros_name =input("----- Second Hero ----- \n Please type your hero's name: ")
    if len(second_heros_name) <= 1:
        print ("Length of hero's name must be longer than 1 character." )       
    elif second_heros_name == first_heros_name:
        print (first_heros_name, "is taken, please choose another name!")

    else:
        print("Second hero's name is"), second_heros_name.capitalize()
        break

players_list = [first_heros_name, second_heros_name]
coin_toss = random.choice(players_list)
players_list.remove(coin_toss)
print ("Coin toss result: %s starts first!" %coin_toss )

def attack1(current_hp):
    hp2=current_hp
    chance_of_damaging=random.randint(0,100)
    print ("--------------- %s Attacks !! ---------------"%coin_toss)
    while True:
        attack_magnitute=input("Choose your attack magnitude between 1 and 50: ")

        if attack_magnitute > 50:
            print ("The attack magnitude must be between 1 and 50.")

        elif attack_magnitute < 1:
            print ("The attack magnitude must be between 1 and 50.")
        else:
            break

def attack2(current_hp):
    hp1=current_hp
    chance_of_damaging=random.randint(0,100)
    print ("--------------- %s Attacks !! ---------------"%players_list)
    while True:
        attack_magnitute=input("Choose your attack magnitude between 1 and 50: ")

        if attack_magnitute > 50:
            print ("The attack magnitude must be between 1 and 50.")

        elif attack_magnitute < 1:
            print ("The attack magnitude must be between 1 and 50.")
        else:
            break


    while True:
        if chance_of_damaging > attack_magnitute:
            print (players_list, " hits %s damage!!"%attack_magnitute)
            hp1=hp1-attack_magnitute
            return hp1
        else:
            print ("Ooopsy! %s missed the attack!"%players_list)
            return hp1

def main():
    hp1, hp2 (100,100)
    while hp2<=1:
        print (players_list, " win")
        break

    while hp1 > 1 and hp2 > 1:
            hp1 = attack1(hp1)
            print ("coin_toss,", "players_list")

            print ("HP [%s]:"%hp2, hp2/2 * "|" ,"        ", "HP [%s]:"%hp1, hp1/2 * "|" )
            hp2 = attack2(hp2)
            print (coin_toss,"     ", players_list)

            print ("HP [%s]:"%hp2, hp2/2 * "|" ,"        ", "HP [%s]:"%hp1, hp1/2 * "|")

    while hp1<=1:
        print (coin_toss, " win")
        brs
    
main()
    while True:
        if chance_of_damaging > attack_magnitute:
            print ("coin_toss,  hits %s damage!!%attack_magnitute")
            hp2=hp2-attack_magnitute
            return hp2
        else:
            print ("Ooopsy! %s missed the attack!"%coin_toss)
            return hp2

