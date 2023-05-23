import tkinter

class Game:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Chess")
        self.root.geometry("500x500")

        self.gameboard = [["" for j in range(8)] for i in range(8)]

        # b - black, w - white
        # p - pawn, n - knight, b - bishop, r - rook, q - queen, k - king
        
        for i in range(8):
            self.gameboard[1][i] = "wp"
            self.gameboard[6][i] = "bp"

        self.gameboard[0][0] = "wr"; self.gameboard[0][7] = "wr"
        self.gameboard[0][1] = "wn"; self.gameboard[0][6] = "wn"
        self.gameboard[0][2] = "wb"; self.gameboard[0][5] = "wb"
        self.gameboard[0][3] = "wq"; self.gameboard[0][4] = "wk"
        
        self.gameboard[7][0] = "br"; self.gameboard[7][7] = "br"
        self.gameboard[7][1] = "bn"; self.gameboard[7][6] = "bn"
        self.gameboard[7][2] = "bb"; self.gameboard[7][5] = "bb"
        self.gameboard[7][3] = "bq"; self.gameboard[7][4] = "bk"

        for i in range(8):
            for j in range(8):
                print("|{:2s}|".format(self.gameboard[i][j]), end = "")
            print("")

        self.gameboard_buttons = []
        for i in range(8):
            self.gameboard_buttons.append([])
            for j in range(8):
                self.gameboard_buttons[i].append(tkinter.Button(self.root, text = "a", font = ('Cantarell', 8)))
                self.gameboard_buttons[i][j].bind('<Button>', self.print_position)
                self.gameboard_buttons[i][j].grid(row = i, column = j)

        self.root.mainloop()

    def print_position(self, event):
        info = event.widget.grid_info()
        print(info["row"], info["column"])
