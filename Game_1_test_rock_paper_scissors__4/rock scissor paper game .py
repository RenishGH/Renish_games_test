from tkinter import *
from PIL import Image, ImageTk
from random import choice

# Constants
BG_COLOR = "light blue"
FONT_COLOR = "red"
MSG_BG = "red"
MSG_FG = "white"

# Main window setup
root = Tk()
root.title("Renish Game Test - Rock Paper Scissors")
root.configure(background=BG_COLOR)

# Load images
rock_img_user = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img_user = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img_user = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# Display labels for user and computer choices
user_label = Label(root, image=scissor_img_user, bg=BG_COLOR)
comp_label = Label(root, image=scissor_img_comp, bg=BG_COLOR)
user_label.grid(row=1, column=4)
comp_label.grid(row=1, column=0)

# Score labels
player_score = Label(root, text=0, font=("Arial", 24), bg=BG_COLOR, fg=FONT_COLOR)
computer_score = Label(root, text=0, font=("Arial", 24), bg=BG_COLOR, fg=FONT_COLOR)
player_score.grid(row=1, column=3)
computer_score.grid(row=1, column=1)

# Indicators
Label(root, font=("Arial", 14), text="USER", bg="black", fg=FONT_COLOR).grid(row=0, column=3)
Label(root, font=("Arial", 14), text="COMPUTER", bg="black", fg=FONT_COLOR).grid(row=0, column=1)

# Message label
msg = Label(root, font=("Arial", 18), bg=MSG_BG, fg=MSG_FG)
msg.grid(row=3, column=2)

# Renish Game Test label
Label(root, text="Renish Game Test", font=("Arial", 18, "bold"), bg=BG_COLOR, fg="black").grid(row=4, column=2, pady=10)

# Update message function
def update_message(message):
    msg['text'] = message

# Update scores
def update_user_score():
    score = int(player_score["text"]) + 1
    player_score["text"] = str(score)

def update_computer_score():
    score = int(computer_score["text"]) + 1
    computer_score["text"] = str(score)

# Check winner
def check_winner(player, computer):
    if player == computer:
        update_message("It's a Tie!")
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
        update_message("You Win!")
        update_user_score()
    else:
        update_message("You Lose!")
        update_computer_score()

# Update choice
def update_choice(user_choice):
    comp_choice = choice(["rock", "paper", "scissor"])

    # Update computer image
    comp_label.configure(image={
        "rock": rock_img_comp,
        "paper": paper_img_comp,
        "scissor": scissor_img_comp
    }[comp_choice])

    # Update user image
    user_label.configure(image={
        "rock": rock_img_user,
        "paper": paper_img_user,
        "scissor": scissor_img_user
    }[user_choice])

    check_winner(user_choice, comp_choice)

# Buttons
Button(root, width=20, height=2, text="ROCK", bg="red", fg="white", command=lambda: update_choice("rock")).grid(row=2, column=1)
Button(root, width=20, height=2, text="PAPER", bg="green", fg="white", command=lambda: update_choice("paper")).grid(row=2, column=2)
Button(root, width=20, height=2, text="SCISSORS", bg="blue", fg="white", command=lambda: update_choice("scissor")).grid(row=2, column=3)

# Start the GUI event loop
root.mainloop()
