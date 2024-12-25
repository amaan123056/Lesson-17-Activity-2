import random
options=["rock","paper,","scissors"]
user_choice=input("rock paper scissor")
ai_choice=random.choice(options)
print("your choice",user_choice)
print("compooter choice",ai_choice)
if user_choice==ai_choice:
    print("pick something else , stoobid")
elif user_choice=="rock" and ai_choice=="scisssors":
    print("another epic victory ")
elif user_choice=="paper" and ai_choice=="rock":
    print("another epic victory ")
elif user_choice=="scissors" and ai_choice=="paper":
    print("another epic victory ")
else:
    print("you cant excpect to win them all")