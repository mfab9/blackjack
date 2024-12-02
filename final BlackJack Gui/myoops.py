from tkinter import *
from tkinter import messagebox as m
from PIL import Image, ImageTk
import random
from pygame import mixer
import time
class BlackjackGame:
    def __init__(self, window):
        self.window = window
        self.window.title("")
        self.window.geometry("800x800")
        self.window.configure(bg="green")

        self.player_hand = 0
        self.dealer_hand = 0
        self.player_sum = 0
        self.dealer_sum = 0
        self.black_jack_status = {"dealer": "no", "player": "no"}
        self.deck = []
        self.dealer = []
        self.player = []
        self.dealer_score = []
        self.player_score = []
        self.card_images = {}  # Dictionary to store card images

        self.game_frame = Frame(self.window, bg="green")
        self.dealer_frame = LabelFrame(self.game_frame, bg="blue", text='dealer hand')
        self.player_frame = LabelFrame(self.game_frame, bg="blue", text="player's hand")
        self.dealer_label_1 = Label(self.dealer_frame, text="")
        self.dealer_label_1.grid(row=0, column=1)
        self.dealer_label_2 = Label(self.dealer_frame, text="")
        self.dealer_label_2.grid(row=0, column=2)
        self.dealer_label_3 = Label(self.dealer_frame, text="")
        self.dealer_label_3.grid(row=0, column=3)
        self.dealer_label_4 = Label(self.dealer_frame, text="")
        self.dealer_label_4.grid(row=0, column=4)
        self.dealer_label_5 = Label(self.dealer_frame, text="")
        self.dealer_label_5.grid(row=0, column=5)

        self.player_label_1 = Label(self.player_frame, text="")
        self.player_label_1.grid(row=0, column=1)
        self.player_label_2 = Label(self.player_frame, text="")
        self.player_label_2.grid(row=0, column=2)
        self.player_label_3 = Label(self.player_frame, text="")
        self.player_label_3.grid(row=0, column=3)
        self.player_label_4 = Label(self.player_frame, text="")
        self.player_label_4.grid(row=0, column=4)
        self.player_label_5 = Label(self.player_frame, text="")
        self.player_label_5.grid(row=0, column=5)

        self.button_frame = Frame(self.window, bg="black")
        self.hit_button = Button(self.button_frame, bg="red", text="HIT", command=self.player_hit)
        self.stand_button = Button(self.button_frame, bg="green", text="STAND", command=self.stand_fn)
        self.start_button = Button(self.button_frame, bg="white", text="START", command=self.start_game)

        self.game_frame.pack()
        self.dealer_frame.pack()
        self.player_frame.pack()
        self.button_frame.pack()
        self.hit_button.pack(side="left")
        self.stand_button.pack(side="left")
        self.start_button.pack(side="left")
        self.start_game()

    def play_sound(self, p="player"):
        mixer.init()  # Initialize the mixer
        if p == "player":
            mixer.music.load("sounds/7 CRORE KBC - SOUND EFFECT.mp3")
            mixer.music.play()
            m.showinfo("WON", f"WON\nPLAYER:{self.player_sum}({len(self.player)})\nDEALER:{self.dealer_sum}({len(self.dealer)})")
            self.window.update_idletasks()
        elif p == "dealer":
            mixer.music.load("sounds/negative_beeps-6008.mp3")
            mixer.music.play()
            m.showinfo("DEALER WINS", f"LOOSE\nDEALER:{self.dealer_sum}({len(self.dealer_score)})\nPLAYER:{self.player_sum}({len(self.player_score)})")
            self.window.update_idletasks()
        elif p == "tie":
            mixer.music.load("sounds/bruh.mp3")
            mixer.music.play()
            m.showinfo("TIE WINS", f"TIE\nPLAYER:{self.player_sum}({len(self.player_score)})\nDEALER:({self.dealer_sum}({len(self.dealer_score)})")
            self.window.update_idletasks()

    def stand_fn(self):
        self.player_sum = sum(self.player_score)
        self.dealer_sum = sum(self.dealer_score)
        self.stand_button.config(state="disabled")
        self.hit_button.config(state="disabled")

        if self.dealer_sum >= 17:
            if self.dealer_sum > 21:
                self.play_sound()
            elif self.dealer_sum == self.player_sum:
                self.play_sound("tie")
            elif self.dealer_sum > self.player_sum:
                self.play_sound("dealer")
            else:
                self.play_sound()
        else:
            self.dealer_hit()  # Call dealer_hit() here
            self.window.after(1000, self.stand_fn)  # Call stand_fn() recursively with a delay

    def start_game(self):
        self.stand_button.config(state="normal")
        self.hit_button.config(state="normal")
        self.black_jack_status = {"dealer": "no", "player": "no"}
        self.dealer = []
        self.player = []
        self.deck = []
        self.dealer_score = []
        self.player_score = []
        suits = ["clubs", "diamonds", "hearts", "spades"]
        ranks = ["queen", "king", "ace", "jack"]
        ranks += [x for x in range(2, 11)]
        for suit in suits:
            for rank in ranks:
                self.deck.append(f"{rank}_of_{suit}")
        self.player_hand = 0
        self.dealer_hand = 0
        self.player_label_1.configure(image="")
        self.player_label_2.configure(image="")
        self.player_label_3.configure(image="")
        self.player_label_4.configure(image="")
        self.player_label_5.configure(image="")
        self.dealer_label_1.configure(image="")
        self.dealer_label_2.configure(image="")
        self.dealer_label_3.configure(image="")
        self.dealer_label_4.configure(image="")
        self.dealer_label_5.configure(image="")
        self.player_hit()
        self.player_hit()
        self.dealer_hit()
        self.dealer_hit()

    def load_card_images(self):
        for card in self.deck:
            image = Image.open(f'Card_deck/{card}.png')
            image = image.resize((150, 218))
            self.card_images[card] = ImageTk.PhotoImage(image)

    def player_hit(self):
        if self.player_hand < 5:
            try:
                player_card = random.choice(self.deck)
                self.deck.remove(player_card)
                self.player.append(player_card)
                pcard = player_card.split("_", 1)[0]
                if pcard == "ace":
                    self.player_score.append(11)
                elif pcard == "jack" or pcard == "queen" or pcard == "king":
                    self.player_score.append(10)
                else:
                    self.player_score.append(int(pcard))

                player_image = self.card_images[player_card]
                getattr(self, f"player_label_{self.player_hand + 1}").configure(image=player_image)  # Configure image
                self.window.title(f"{len(self.deck)} cards left")
                self.player_hand += 1

            except:
                self.window.title("no cards left")
            self.black_jack("player")

    def dealer_hit(self):
        if self.dealer_hand < 5:
            try:
                dealer_card = random.choice(self.deck)
                self.deck.remove(dealer_card)
                self.dealer.append(dealer_card)
                dcard = dealer_card.split("_", 1)[0]
                if dcard == "ace":
                    self.dealer_score.append(11)
                elif dcard == "jack" or dcard == "queen" or dcard == "king":
                    self.dealer_score.append(10)
                else:
                    self.dealer_score.append(int(dcard))

                dealer_image = self.card_images[dealer_card]
                getattr(self, f"dealer_label_{self.dealer_hand + 1}").configure(image=dealer_image)  # Configure image
                self.window.title(f"{len(self.deck)} cards left")
                self.dealer_hand += 1

            except:
                self.window.title("no cards left")
            self.black_jack("dealer")

    def black_jack(self, player):
        self.player_sum = 0
        self.dealer_sum = 0
        if player == "dealer":
            if len(self.dealer_score) == 2:
                if self.dealer_score[0] + self.dealer_score[1] == 21:
                    self.black_jack_status["dealer"] = "yes"
        if player == "player":
            if len(self.player_score) == 2:
                if self.player_score[0] + self.player_score[1] == 21:
                    self.black_jack_status["player"] = 'yes'
            else:
                self.player_sum = sum(self.player_score)
                if self.player_sum == 21:
                    self.black_jack_status["player"] = 'yes'
                elif self.player_sum > 21:
                    for i, card in enumerate(self.player_score):
                        if card == 11:
                            self.player_score[i] = 1
                            self.player_sum = 0
                            self.player_sum = sum(self.player_score)
                            if self.player_sum > 21:
                                self.black_jack_status["player"] = 'bust'
                    else:
                        if self.player_sum == 21:
                            self.black_jack_status["player"] = "yes"
                        if self.player_sum > 21:
                            self.black_jack_status["player"] = 'bust'

        if len(self.dealer_score) == 2 and len(self.player_score) == 2:
            if self.black_jack_status['player'] == "yes" and self.black_jack_status["dealer"] == "yes":
                self.stand_button.config(state="disabled")
                self.hit_button.config(state="disabled")
                self.play_sound("tie")
            elif self.black_jack_status["player"] == "yes":
                self.stand_button.config(state="disabled")
                self.hit_button.config(state="disabled")
                self.play_sound()
            elif self.black_jack_status["dealer"] == "yes":
                self.stand_button.config(state="disabled")
                self.hit_button.config(state="disabled")
                m.showinfo("BLACKJACK!!!", f"LOOSE FROM BJ\nDEALER:({len(self.dealer_score)})\nPLAYER:{self.player_sum}({len(self.player_score)})")

        else:
            if self.black_jack_status['player'] == "yes" and self.black_jack_status["dealer"] == "yes":
                self.stand_button.config(state="disabled")
                self.hit_button.config(state="disabled")
                self.play_sound("tie")
            elif self.black_jack_status["player"] == "yes":
                self.stand_button.config(state="disabled")
                self.hit_button.config(state="disabled")
                self.play_sound()
            elif self.black_jack_status["dealer"] == "yes":
                self.stand_button.config(state="disabled")
                self.hit_button.config(state="disabled")
                self.play_sound("dealer")

        if self.black_jack_status["player"] == 'bust':
            self.stand_button.config(state="disabled")
            self.hit_button.config(state="disabled")
            self.play_sound("tie")

    def resize_cards(self, path):
        pic = Image.open(path)
        new_pic = pic.resize((150, 218))
        pic = ImageTk.PhotoImage(new_pic)
        return pic


if __name__ == "__main__":
    window = Tk()
    game = BlackjackGame(window)
    game.load_card_images()  # Load card images
    window.mainloop()
