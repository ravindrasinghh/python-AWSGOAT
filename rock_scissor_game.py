import emoji

print("Rock")
print("Paper")
print("scissor")

Player1 = input("Player 1: Enter your move: ")
Player2 = input("Player 2: Enter your move: ")

if Player1 == "Rock" and Player2 == "Paper":
    print(emoji.emojize("Player1 wins:thumbs_up:"))
elif Player1 == "Rock" and Player2 == "scissor":
    print(emoji.emojize("Player1 wins:thumbs_up:"))
elif Player1 == "Paper" and Player2 == "scissor":
    print("Player1 wins")
elif Player1 == Player2:
    print(emoji.emojize("TIE:handshake:"))    
else:
    print("Wrong move")        
    
##FOR EMOJI
#https://unicode.org/emoji/charts/emoji-list.html
##  
    
