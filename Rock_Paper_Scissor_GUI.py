import tkinter as tk
from tkinter import messagebox
import random

rock = '''
    _______
---'   ____ )
      (_____ )
      (_____ )
      (____ )
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ["Rock", "Paper", "Scissors"]
ascii_art = [rock, paper, scissor]

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.configure(bg="#1a1a2e")
        self.player_score = 0
        self.computer_score = 0

        title = tk.Label(root, text="🎮 ROCK–PAPER–SCISSORS 🎮", font="Consolas 28 bold", fg="#eee", bg="#1a1a2e")
        title.pack(pady=20)

        score_frame = tk.Frame(root, bg="#16213e", relief=tk.RAISED, bd=3)
        score_frame.pack(pady=10)
        self.score_label = tk.Label(score_frame, text="Player: 0   Computer: 0", font="Consolas 20 bold", fg="#00ff41", bg="#16213e", padx=30, pady=15)
        self.score_label.pack()

        result_frame = tk.Frame(root, bg="#0f3460", relief=tk.SUNKEN, bd=2, height=350)
        result_frame.pack(pady=15, padx=40, fill=tk.X)
        result_frame.pack_propagate(False)
        self.result_label = tk.Label(result_frame, text="Choose your move!", font="Consolas 14", fg="#f5f5f5", bg="#0f3460", justify="left", padx=20, pady=20)
        self.result_label.pack()

        btn_frame = tk.Frame(root, bg="#1a1a2e")
        btn_frame.pack(pady=15)

        rock_btn = tk.Button(btn_frame, text="🪨 Rock", width=15, height=2, font="Consolas 14 bold", 
                            bg="#e94560", fg="white", activebackground="#c23b52", 
                            relief=tk.RAISED, bd=4, cursor="hand2", command=lambda: self.play(0))
        paper_btn = tk.Button(btn_frame, text="📄 Paper", width=15, height=2, font="Consolas 14 bold", 
                             bg="#533483", fg="white", activebackground="#442a6a", 
                             relief=tk.RAISED, bd=4, cursor="hand2", command=lambda: self.play(1))
        scissor_btn = tk.Button(btn_frame, text="✂️ Scissors", width=15, height=2, font="Consolas 14 bold", 
                               bg="#16a085", fg="white", activebackground="#138871", 
                               relief=tk.RAISED, bd=4, cursor="hand2", command=lambda: self.play(2))

        rock_btn.grid(row=0, column=0, padx=15, pady=10)
        paper_btn.grid(row=0, column=1, padx=15, pady=10)
        scissor_btn.grid(row=0, column=2, padx=15, pady=10)

        restart_btn = tk.Button(root, text="🔄 Restart Game", font="Consolas 14 bold", 
                               bg="#f39c12", fg="white", activebackground="#d68910", 
                               relief=tk.RAISED, bd=3, cursor="hand2", padx=20, pady=10, command=self.restart_game)
        restart_btn.pack(pady=15)

    def play(self, player_choice):
        computer_choice = random.randint(0, 2)

        result_text = f"Your Choice:\n{ascii_art[player_choice]}\n\nComputer's Choice:\n{ascii_art[computer_choice]}\n"

        if player_choice == computer_choice:
            result_text += "\n🤝 It's a Draw!"
        elif (player_choice == 0 and computer_choice == 2) or \
             (player_choice == 1 and computer_choice == 0) or \
             (player_choice == 2 and computer_choice == 1):
            result_text += "\n🎉 You Won!"
            self.player_score += 1
        else:
            result_text += "\n💻 Computer Won!"
            self.computer_score += 1

        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Player: {self.player_score}   Computer: {self.computer_score}")

    def restart_game(self):
        if messagebox.askyesno("Restart Game", "Do you want to restart the game?"):
            self.player_score = 0
            self.computer_score = 0
            self.score_label.config(text="Player: 0   Computer: 0")
            self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    game = RPSGame(root)
    root.mainloop()
