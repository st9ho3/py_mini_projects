name = input("Type your name: ")
print("Welcome",name,"to this adventure!")

answer =input("You are on a dirt road, it has come to an end and you can go left or right. Which way you want to go?").lower()
if answer == "left" :
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")
    if answer == "swim" :
        print("You swim accross and were eaten by an alligator")
    elif answer == "walk" :
        print("You walked for many miles, ran out of water and lost the game. ")
    else :
        print("Not a valid option. You lose")
elif answer == "right" :
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? ")
    if answer == "back" :
        print("You go back to the main road.Now you can decide to drive back")
    elif answer == "cross" :
        answer = input("You cross the bridge and meet a strager. Do you talk to them? Y or No")
        if answer == "Y" :
            print("You talk to the stranger and you get some gold.")
        elif answer == "N" :
            print("You ignore the stranger and they're offended. You lose")
        print("You walked for many miles, ran out of water and lost the game. ")
    else :
        print("Not a valid option. You lose")
else :
    print('Not a valid option.You lose.')
