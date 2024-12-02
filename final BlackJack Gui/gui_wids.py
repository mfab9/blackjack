from tkinter import *
from tkinter import messagebox as m
from PIL import Image, ImageTk
import random
from pygame import mixer
import time




def play_sound(p="player"):
    mixer.init()  # Initialize the mixer
    if p=="player":
        mixer.music.load("sounds/7 CRORE KBC - SOUND EFFECT.mp3")
        mixer.music.play()
        m.showinfo("WON",f"WON\nPLAYER:{player_sum}({len(player)})\nDEALER:{dealer_sum}({len(dealer)})")
        window.update_idletasks()
    elif p=="dealer":
        mixer.music.load("sounds/negative_beeps-6008.mp3")
        mixer.music.play()
        m.showinfo("DEALER WINS", f"LOOSE\nDEALER:{dealer_sum}({len(dealer_score)})\nPLAYER:{player_sum}({len(player_score)})")
        window.update_idletasks()
    elif p=="tie":
        mixer.music.load("sounds/bruh.mp3")
        mixer.music.play()
        m.showinfo("TIE WINS", f"TIE\nPLAYER:{player_sum}({len(player_score)})\nDEALER:({dealer_sum}({len(dealer_score)})")
        window.update_idletasks()
window = Tk()
window.title("")
window.geometry("800x800")
window.configure(bg="green")


# fn
def stand_fn():
    global player_sum, dealer_sum, player_score, dealer_score
    player_sum = 0
    dealer_sum = 0
    player_sum = sum(player_score)
    dealer_sum = sum(dealer_score)
    stand_button.config(state="disabled")
    hit_button.config(state="disabled")
    if dealer_sum >= 17:
        if dealer_sum > 21:
            #m.showinfo("PLAYER WINS", f"WON\nDEALER:{dealer_sum}\nPLAYER:{player_sum}(1)")
            play_sound()
        elif dealer_sum == player_sum:
            #m.showinfo("TIE", f"TIE\nDEALER:{dealer_sum}({len(dealer_score)})\nPLAYER:{player_sum}({len(player_score)})")
            play_sound("tie")
        elif dealer_sum > player_sum:

            #m.showinfo("DEALER WINS", f"LOOSE\nDEALER:{dealer_sum}({len(dealer_score)})\nPLAYER:{player_sum}({len(player_score)})")
            play_sound("dealer")
        else:
            #m.showinfo("PLAYER WINS", f"WON\nDEALER:{dealer_sum}\nPLAYER:{player_sum}(4)")
            play_sound()

    else:
        dealer_hit()
        stand_fn()


def start_game():
    stand_button.config(state="normal")
    hit_button.config(state="normal")
    global black_jack_status, player_sum, dealer_sum

    player_sum = 0
    dealer_sum = 0
    black_jack_status = {"dealer": "no", "player": "no"}

    global player_hand, dealer_hand, dealer, player, player_score, dealer_score, deck
    dealer = []
    player = []
    deck = []
    dealer_score = []
    player_score = []
    suits = ["clubs", "diamonds", "hearts", "spades"]
    ranks = ["queen", "king", "ace", "jack"]
    ranks += [x for x in range(2, 11)]
    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank}_of_{suit}")
    player_hand = 0
    dealer_hand = 0
    player_label_1.configure(image="")
    player_label_2.configure(image="")
    player_label_3.configure(image="")
    player_label_4.configure(image="")
    player_label_5.configure(image="")

    dealer_label_1.configure(image="")
    dealer_label_2.configure(image="")
    dealer_label_3.configure(image="")
    dealer_label_4.configure(image="")
    dealer_label_5.configure(image="")

    player_hit()
    player_hit()
    dealer_hit()
    dealer_hit()

def resize_cards(path):
    pic = Image.open(path)
    new_pic = pic.resize((150, 218))
    pic = ImageTk.PhotoImage(new_pic)
    return pic


def black_jack(player):
    global player_sum, dealer_sum ,player_score#dealer_score
    player_sum = 0
    dealer_sum = 0

    if player == "dealer":
        if len(dealer_score) == 2:
            if dealer_score[0] + dealer_score[1] == 21:
                black_jack_status["dealer"] = "yes"
    if player == "player":
        if len(player_score) == 2:
            if player_score[0] + player_score[1] == 21:
                black_jack_status["player"] = "yes"
        else:
            player_sum = sum(player_score)
            if player_sum == 21:
                black_jack_status["player"] = 'yes'
            elif player_sum > 21:
                for i, card in enumerate(player_score):
                    if card == 11:
                        player_score[i] = 1
                        player_sum = 0
                        player_sum = sum(player_score)
                        if player_sum > 21:
                            black_jack_status["player"] = 'bust'
                else:
                    if player_sum == 21:
                        black_jack_status["player"] = "yes"
                    if player_sum > 21:
                        black_jack_status["player"] = 'bust'


    if len(dealer_score) == 2 and len(player_score) == 2:
        if black_jack_status['player'] == "yes" and black_jack_status["dealer"] == "yes":
            stand_button.config(state="disabled")
            hit_button.config(state="disabled")
            #window.update_idletasks()
            #m.showinfo("TIE ", f"TIE \nPLAYER:{player_sum}({len(player_score)})\nDEALER:{dealer_sum}({len(dealer_score)})")
            play_sound("tie")
        elif black_jack_status["player"] == "yes":
            stand_button.config(state="disabled")
            hit_button.config(state="disabled")
            #window.update_idletasks()
            # time.sleep(2)
            #m.showinfo("BLACKJACK!!!", f"WON FROM BJ\ndealer:{dealer_sum}\nPlayer Wins{player_sum}(6)")
            play_sound()

        elif black_jack_status["dealer"] == "yes":
            stand_button.config(state="disabled")
            hit_button.config(state="disabled")
            #window.update_idletasks()
            # time.sleep(2)
            m.showinfo("BLACKJACK!!!", f"LOOSE FROM BJ\nDEALER:({len(dealer_score)})\nPLAYER:{player_sum}({len(player_score)})")

    else:

        if black_jack_status['player'] == "yes" and black_jack_status["dealer"] == "yes":
            stand_button.config(state="disabled")
            hit_button.config(state="disabled")
            #window.update_idletasks()
            # time.sleep(2)
            #m.showinfo("TIE ", f"TIE alL BJ\nDEALER:({len(dealer_score)})\nPLAYER:{player_sum}({len(player_score)})")
            play_sound("tie")
        elif black_jack_status["player"] == "yes":
            stand_button.config(state="disabled")
            hit_button.config(state="disabled")
            #window.update_idletasks()
            #  time.sleep(2)
            play_sound()
            #m.showinfo("21!!!", f"WON FROM BJ\nDEALER\n{dealer_sum}:Player Wins:{player_sum}(9)")
        elif black_jack_status["dealer"] == "yes":
            stand_button.config(state="disabled")
            hit_button.config(state="disabled")
            #window.update_idletasks()
            #   time.sleep(2)
            #m.showinfo("21!!!", f"LOOSE FROM BJ\nLOOSE\n{dealer_sum}({len(dealer_score)})\nPLAYER:{player_sum}({len(player_score)})")
            play_sound("dealer")

    if black_jack_status["player"] == 'bust':
        stand_button.config(state="disabled")
        hit_button.config(state="disabled")
        #window.update_idletasks()
        play_sound("tie")
        # time.sleep(2)
        #m.showinfo("BUSTED!!!", f"BUSTED\nDEALER:{dealer_sum}{len(player_score)}\nPLAYER:{player_sum}({len(dealer_score)})")


def player_hit():

    global player_hand
    if player_hand < 5:
        try:
            player_card = random.choice(deck)
            deck.remove(player_card)
            player.append(player_card)
            pcard = player_card.split("_", 1)[0]
            if pcard == "ace":
                player_score.append(11)
            elif pcard == "jack" or pcard == "queen" or pcard == "king":
                player_score.append(10)
            else:
                player_score.append(int(pcard))

            global player_image_1, player_image_2, player_image_3, player_image_4, player_image_5
            if player_hand == 0:
                player_image_1 = resize_cards(f'Card_deck/{player_card}.png')
                player_label_1.config(image=player_image_1)
                window.title(f"{len(deck)} cards left")
                player_hand += 1
            elif player_hand == 1:
                player_image_2 = resize_cards(f'Card_deck/{player_card}.png')
                player_label_2.config(image=player_image_2)
                window.title(f"{len(deck)} cards")
                player_hand += 1
            elif player_hand == 2:
                player_image_3 = resize_cards(f'Card_deck/{player_card}.png')
                player_label_3.config(image=player_image_3)
                window.title(f"{len(deck)} cards left")
                player_hand += 1
            elif player_hand == 3:
                player_image_4 = resize_cards(f'Card_deck/{player_card}.png')
                player_label_4.config(image=player_image_4)
                window.title(f"{len(deck)} cards left")
                player_hand += 1
            elif player_hand == 4:
                player_image_5 = resize_cards(f'Card_deck/{player_card}.png')
                player_label_5.config(image=player_image_5)
                window.title(f"{len(deck)} cards left")
                player_hand += 1

        except:
            window.title("no cards left")
        black_jack("player")


def dealer_hit():
    global dealer_hand
    if dealer_hand <5:
        try:
            dealer_card = random.choice(deck)
            deck.remove(dealer_card)
            dealer.append(dealer_card)
            dcard = dealer_card.split("_", 1)[0]
            if dcard == "ace":
                dealer_score.append(11)
            elif dcard == "jack" or dcard == "queen" or dcard == "king":
                dealer_score.append(10)
            else:
                dealer_score.append(int(dcard))

            global dealer_image_1, dealer_image_2, dealer_image_3, dealer_image_4, dealer_image_5
            if dealer_hand == 0:
                dealer_image_1 = resize_cards(f'Card_deck/{dealer_card}.png')
                dealer_label_1.config(image=dealer_image_1)
                window.title(f"{len(deck)} cards left")
                dealer_hand += 1
            elif dealer_hand == 1:
                dealer_image_2 = resize_cards(f'Card_deck/{dealer_card}.png')
                dealer_label_2.config(image=dealer_image_2)
                window.title(f"{len(deck)} cards")
                dealer_hand += 1
            elif dealer_hand == 2:
                dealer_image_3 = resize_cards(f'Card_deck/{dealer_card}.png')
                dealer_label_3.config(image=dealer_image_3)
                window.title(f"{len(deck)} cards left")
                dealer_hand += 1
            elif dealer_hand == 3:
                dealer_image_4 = resize_cards(f'Card_deck/{dealer_card}.png')
                dealer_label_4.config(image=dealer_image_4)
                window.title(f"{len(deck)} cards left")
                dealer_hand += 1
            elif dealer_hand == 4:
                dealer_image_5 = resize_cards(f'Card_deck/{dealer_card}.png')
                dealer_label_5.config(image=dealer_image_5)
                window.title(f"{len(deck)} cards left")
                dealer_hand += 1


        except:
            window.title("no cards left")
        black_jack("dealer")


game_frame = Frame(window, bg="green")
dealer_frame = LabelFrame(game_frame, bg="blue", text='dealer hand')
player_frame = LabelFrame(game_frame, bg="blue", text="player's hand")
dealer_label_1 = Label(dealer_frame, text="")
dealer_label_1.grid(row=0, column=1)
dealer_label_2 = Label(dealer_frame, text="")
dealer_label_2.grid(row=0, column=2)
dealer_label_3 = Label(dealer_frame, text="")
dealer_label_3.grid(row=0, column=3)
dealer_label_4 = Label(dealer_frame, text="")
dealer_label_4.grid(row=0, column=4)
dealer_label_5 = Label(dealer_frame, text="")
dealer_label_5.grid(row=0, column=5)

player_label_1 = Label(player_frame, text="")
player_label_1.grid(row=0, column=1)

player_label_2 = Label(player_frame, text="")
player_label_2.grid(row=0, column=2)

player_label_3 = Label(player_frame, text="")
player_label_3.grid(row=0, column=3)

player_label_4 = Label(player_frame, text="")
player_label_4.grid(row=0, column=4)

player_label_5 = Label(player_frame, text="")
player_label_5.grid(row=0, column=5)

button_frame = Frame(window, bg="black")
hit_button = Button(button_frame, bg="red", text="HIT", command=player_hit)
stand_button = Button(button_frame, bg="green", text="STAND", command=stand_fn)
start_button = Button(button_frame, bg="white", text="START", command=start_game)
# Layout
game_frame.pack()
dealer_frame.pack()
player_frame.pack()
button_frame.pack()
hit_button.pack(side="left")
stand_button.pack(side="left")
start_button.pack(side="left")
start_game()
window.mainloop()
