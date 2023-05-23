import tkinter
from PIL import ImageTk, Image
from logic.chess import Game

class StartScreen:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Chess")
        self.root.geometry("300x300")

        cover_image = Image.open("./images/cover.png")
        cover_image = cover_image.resize((300, 144), Image.Resampling.LANCZOS)
        cover_image = ImageTk.PhotoImage(cover_image, master = self.root)

        self.title_label = tkinter.Label(self.root, text = "Chess", font = ('Cantarell', 24))
        self.cover_label = tkinter.Label(self.root, image = cover_image)
        self.play_btn = tkinter.Button(self.root, text = "Play", font = ('Cantarell', 18), command = self.play)
        self.quit_btn = tkinter.Button(self.root, text = "Exit", font = ('Cantarell', 18), command = self.quit)

        self.title_label.pack(pady = 10)
        self.cover_label.pack(pady = 0)
        self.play_btn.pack(fill = 'x')
        self.quit_btn.pack(fill = 'x')

        self.root.mainloop()

    def play(self):
        Game()

    def quit(self):
        self.root.destroy()


StartScreen()
