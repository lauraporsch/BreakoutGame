from tkinter import *


class PopUp(Tk):
    def __init__(self):
        """initiates class PopUp, creates a window with the explanation text"""
        super().__init__()
        self.title("Breakout Game")
        self.geometry("1200x500")
        self.config(bg="black")
        self.create_text()
        self.mainloop()

    def create_text(self):
        """creates the labels heading and explanation and a button that starts the game on click"""
        heading = Label(text="Welcome to my version of the famous Breakout Game", font=("Courier", 25, "bold"),
                        background="black", foreground="white")
        heading.place(x=100, y=100)

        explanation = Label(text="1. Use the Left and Right Buttons on your keyboard to move the paddle\n2. Try to "
                                 "destroy all bricks.\n3. If the paddle misses the ball you loose one life.\n4. You "
                                 "have 3 lives.\n\nCan you beat the High Score?", font=("Courier", 15),
                            background="black", foreground="white", justify="left")
        explanation.place(x=300, y=200)

        start_button = Button(text="START GAME", font=("Courier", 15, "bold"), command=self.start_game)
        start_button.place(x=400, y=400)

    def start_game(self):
        """brings popup window to the back and opens game screen, returns True to trigger game start"""
        self.quit()
        return True
