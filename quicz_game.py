print("Welcome to my Quizz!!")

playing = input("Do You want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay!! Let's Play :) ")      
score = 0

answer = input("What does CPU stand for? ")
answer = answer.lower()
if answer == "central processing unit":
    print("Correct Answer!!")
    score += 1
else: 
    print("Oops!! Incorrect Answer")

answer = input("What does GPU stand for? ")
answer = answer.lower()
if answer == "graphics processing unit":
    print("Correct Answer!!")
    score += 1
else: 
    print("Oops!! Incorrect Answer")


answer = input("What does RAM stand for? ")
answer = answer.lower()
if answer == "random access memory":
    print("Correct Answer!!")
    score += 1
else: 
    print("Oops!! Incorrect Answer")

answer = input("What does PSU stand for? ")
answer = answer.lower()
if answer == "power supply":
    print("Correct Answer!!")
    score += 1
else: 
    print("Oops!! Incorrect Answer")

print("You Got a score of: " + str(score) +" ! Congratulations ")
print("You Got: " + str((score/4)*100) +"% questions correct!")






    
