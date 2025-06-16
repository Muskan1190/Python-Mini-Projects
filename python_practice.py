#Dice rolling game
import random 
count = 0

while True:
    y_or_n = input("Roll the dice? (y/n): ")
    if y_or_n == 'y':
        random_num = random.randint(1,6)
        random_num2 = random.randint(1,6)
        count +=1
        print("( ",random_num,  " , ", random_num2, " )", "Count: ", count)
    else:
        break

number guessing game
import random

randomi = random.randint(1, 100)  # Fixed range & generated once
count = 0
attempt = 0
while attempt < 5:
    guess = int(input("Please guess a number between 0 to 100: "))
    count += 13
    attempt +=1

    if guess == randomi:
        print(f"You got it babe! It took you {count} tries.")
        break
    elif guess < randomi:
        print("Oh no such a bummer, little higher!")
    else:
        print("Oh girlie, a little lower!")
print("No worries better luck next time! Your attempts are over...")

'''
1. Ask the user to make a choice
2. If the choice is invalid
    Print an error
3. Let the computer to make a choice
    print choices
4. Determine the winner
5.Ask the user if they want to continue
6.If not
    terminate'''
import random
#we can use dictionary to map data and values: 'r' to rock
emojis = { "r": "✊","p": "🤚","s": "✌️"}
choices = ('r','p','s') #converting to tuples so no one removes anything

while True:
    user_choice = input("Rock, Paper, Scissors? (r,p,s): ").lower()
    if user_choice not in choices:
        print("invalid message")
        continue
    
    comp_choice = random.choice(choices)
    
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[comp_choice]}")
    
    if user_choice == comp_choice:
        print("Tie!")
    elif ((user_choice == 'r'and comp_choice == 's') or
          (user_choice == 's'and comp_choice == 'p') or
          (user_choice == 'p'and comp_choice == 'r')):
        print("you win")
    else:
        print("you loose")
        
    continue_user = input("continue or not? ").lower()
    if continue_user == 'n':
        break
    else:
        continue

# making a qr code
pip install qrcode[pill]
import qrcode
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
customer_input = input("Please input a website or text for qr code generation: ")
name_qr_code= input("What name would you like to save it as? ")
img = qrcode.make(customer_input)
qr.make(fit = True)
qr.make_image(fill_color="lavender",back_color="red")
type(img)
img.save(name_qr_code)
import os
print("QR code saved to:", os.getcwd())

#creating a quiz game
questions = int(input("Enter amount of questions to play: "))
score = 0
while True:
    question1 = input("Question 1: What is the capital of France? \n a. Paris\n b. London\n c. Rome  \n Answer: ")
    if question1 == 'a' or question1 == 'Paris':
        print("correct answer")
        score =+ 1 
        print('\n')
    else:
        print("incorrect answer")
        break
    question2 = input("Question 3: What is the capital of England? \n a. Paris\n b. London\n c. Rome  \n Answer:")
    if question2 == 'b' or question2 =='London' or  question2 =='london':
        print("correct answer")
        score +=1 
        print('\n')
    else:
        print("incorrect answer")
        break
    question3 = input("Question 3: What is the capital of India? \n a. Mumbai\n b. New Delhi\n c. Gujarat  \n Answer:")
    if question3 == 'b' or question3 == 'Gujarat' or question3 == 'gujarat':
        print("correct answer")
        score += 1 
        print('\n')
        break
    else:
        print("incorrect answer")
        break
print(f"Your final score: {score")

#To do list application

task= []
while True:
    
    print("To Do List Application: ")
    print("1. 📋 View Tasks")
    print("2. ➕ Add a Task")
    print("3. 🗑️ Remove a Task")
    print("4. 🚪 Exit")
    
    choice = int(input("Please enter your choice (1,2,3,4): "))
   
    if choice == 1:
        if not task:
            print("There are no tasks! 📭")
            break
        else: 
            for idx,t in enumerate(task):
                print(f"🔹{idx + 1}: {t}")
                break
    elif choice == 2:
        user_task = input("which task to add? : ")
        task.append(user_task)
        print(f"Task added: {task}🆕 / ✍️")
    elif choice == 3:
        if not task:
            print("There are no tasks at the moment!")
        else:
            for idx,t in enumerate(task):
                print(f"{idx + 1}: {t}")
            deletion = int(input("What do you want to delete? "))
            if deletion >= 1 and deletion <= len(task): #line checks that input is greater than 1 but smaller than the length of tasks/indexes
                removed = task.pop(deletion-1) #deletion -1 because task stores starting with index 0 so deletion-1 means that we will have 0th index as 1st
                print("Task completed successfully ✅ / 🗑️")
            else:
                print("Invalid number")
                break
    else:
        print("Exiting...👋")
        break


#Creating a pig game
import random
player_1=0
player_2=0
score_player_1 = 0
score_player_2= 0
def player1():
    pl_1= print("Player 1: It is your turn")
    global score_player_1
    while True:
        dice = input("Do you want to roll the dice? (y/n): ")
        if dice.lower() in ['y','yes']:
            if dice == 1:
                print("Oh no, you rolled a 1")
                break
            else:
                randomized = random.randint(1,6)
                print(f"You rolled a: {randomized}")
                score_player_1 = score_player_1+randomized
        elif dice.lower() in ['n','no']:
            print("Thanks for playing")
            break
    print(score_player_1) 
    pl_1= print("Player 2: It is your turn")

def player2(): 
    global score_player_2
    while True:
        dice = input("Do you want to roll the dice? (y/n): ")
        if dice.lower() in ['y','yes'] :
            if dice == 1:
                print("sorry you rolled a 1")
                break
            else:
                randomized_2 = random.randint(1,6)
                print(f"You rolled a: {randomized_2}")
                score_player_2 = score_player_2+randomized_2
        elif dice == 'n':
            print("Thanks for playing")
            break
    print(score_player_2) 
        
def main():
    player_1 = player1()
    player_2 = player2()
    if score_player_1 > score_player_2:
        print(f"Player 1 wins by {score_player_1}")
    elif score_player_1 == score_player_2:
        print(f"Player 1 & Player 2 tie with {score_player_2}")
    else:
        print(f"Player 2 wins by {score_player_2}")
        

#if __name__ == "__main__":
main()
    

import random
from random import choice
import string
chars = string.digits #provides all digits as string
random = "".join(choice(chars) for x in range(4)) #combines randomly chosen digits into a single string and loops 4 times
random_list= list(map(int, str(random)))
print("I have generated a 4 digit number ")    

cow_counter = 0
bull_counter = 0

while True:
    user_input= (int(input("Please enter 4 number: ")))
    user_input_list = list(map(int, str(user_input)))
    if len(user_input_list) > 4:
        break    
    else: 
        for i in user_input_list:
            if i in random_list:
                cow_counter +=1 
        for i ,(a,b) in enumerate(zip(user_input_list,random_list)):
            bull_counter +=1 
        #    print(f"{cow_counter} cows, {bull_counter} bulls")
                
    print(f"{cow_counter} cows, {bull_counter} bulls")
    
import sys

# write your answer here
input1 = input("Enter a string: ")
counter = 0
previous_char = input1[0]
result = []

for i in input1[1:]:
    if i == previous_char:
        counter+=1
    else:
        if counter >= 3 and previous_char not in result:
            result.append(previous_char)
        previous_char = i
        counter = 1

if counter >= 3 and previous_char not in result:
    result.append(previous_char)

output = ''.join(result)
print("Output:", output)
            
#Given a string, print all characters that appear exactly twice consecutively (e.g., 'aabbccdde' → 'abc').
text = "aabbccccd"
result = []
counter = 0
previous_char = text[0]

for i in text[1:]:
    if i == previous_char:
        counter +=1
    else:
        if counter <= 2 and previous_char not in result:
            result.append(previous_char) 
        previous_char = i
        counter = 1
    
print(result)
    
    
 
    
    
    
    
    


