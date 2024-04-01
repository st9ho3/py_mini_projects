print("Welcome to my computer quiz")

playing = input("Do you want to play ? ").lower()
score = 0

if playing != "yes" :
    quit()
print("Okay! Let's play :)")

answer = input("What does CPU stand for ? ").lower()
if answer == "central processing unit" :
    print("Correct !!!")
    score += 1
else :
    print("I'm sorry, your answer is wrong !!!")

answer = input("What does GPU stand for ? ").lower()
if answer == "graphics processing unit" :
    print("Correct !!!")
    score += 1
else :
    print("I'm sorry, your answer is wrong !!!")

answer = input("What does RAM stand for ? ").lower()
if answer == "random access memory" :
    print("Correct !!!")
    score += 1
else :
    print("I'm sorry, your answer is wrong !!!")

answer = input("What does PSU stand for ? ").lower()
if answer == "power supply" :
    print("Correct !!!")
    score += 1
else :
    print("I'm sorry, your answer is wrong !!!")

print("You answered", score,"questions")
print("Your score is", round(score/4*100), "%")