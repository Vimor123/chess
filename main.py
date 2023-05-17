import tkinter
from logic.chess import Game

class StartScreen:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Chess")
        self.root.geometry("300x300")

        self.title_label = tkinter.Label(self.root, text = "Chess", font = ('Cantarell', 24))
        self.play_btn = tkinter.Button(self.root, text = "Play", font = ('Cantarell', 18), command = self.play)
        self.quit_btn = tkinter.Button(self.root, text = "Exit", font = ('Cantarell', 18), command = self.quit)

        self.title_label.pack(pady = 10)
        self.play_btn.pack(fill = 'x')
        self.quit_btn.pack(fill = 'x')

        self.root.mainloop()

    def play(self):
        Game()

    def quit(self):
        self.root.destroy()


StartScreen()
