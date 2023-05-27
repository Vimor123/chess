import tkinter
import time
from PIL import ImageTk, Image
import logic.rules

dark_color = "#C28F58"
light_color = "#F3D1AC"
highlight_dark_color = "#5DD3B8"
highlight_light_color = "#9BF7E2"
tile_size = 50

class Game:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Chess")

        boardsize_string = str(tile_size * 8) + "x" + str(tile_size * 8)
        
        self.root.geometry(boardsize_string)

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

        self.init_images()

        self.gameboard_buttons = []
        for i in range(8):
            self.gameboard_buttons.append([])
            for j in range(8):
                self.gameboard_buttons[i].append(tkinter.Button(self.root, bd = 0,
                                                                highlightthickness = 0))
                self.gameboard_buttons[i][j].bind('<Button>', self.click_tile)
                self.gameboard_buttons[i][j].grid(row = i, column = j)

        self.turn = "w"
        self.phase = "pick_piece"
        self.chosen_piece_position = (-1, -1)
        self.possible_moves = []

        # Used only for en passant
        self.last_move_positions = ((-1, -1), (-1, -1))

        self.render_board(self.turn)

        self.root.mainloop()
        

    def click_tile(self, event):
        info = event.widget.grid_info()
        coords = (-1, -1)
        if self.turn == "w":
            coords = (7 - info["row"], info["column"])
        else:
            coords = (info["row"], 7 - info["column"])

        if self.phase == "pick_piece":
            if self.gameboard[coords[0]][coords[1]].startswith(self.turn):
                moves = logic.rules.get_legal_moves(self.gameboard, self.turn, coords, self.last_move_positions)
                if len(moves) > 0:
                    self.phase = "choose_move"
                    
                    if (info["row"] % 2 == 0 and info["column"] % 2 == 0) or (info["row"] % 2 == 1 and info["column"] % 2 == 1):
                        self.gameboard_buttons[info["row"]][info["column"]].config(bg = highlight_light_color, activebackground = highlight_light_color)
                    else:
                        self.gameboard_buttons[info["row"]][info["column"]].config(bg = highlight_dark_color, activebackground = highlight_dark_color)
                        
                    for move in moves:
                        if self.turn == "w":
                            button_coords = (7 - move[0], move[1])
                        else:
                            button_coords = (move[0], 7 - move[1])
                            
                        if (button_coords[0] % 2 == 0 and button_coords[1] % 2 == 0) or (button_coords[0] % 2 == 1 and button_coords[1] % 2 == 1):
                            self.gameboard_buttons[button_coords[0]][button_coords[1]].config(bg = highlight_light_color, activebackground = highlight_light_color)
                        else:
                            self.gameboard_buttons[button_coords[0]][button_coords[1]].config(bg = highlight_dark_color, activebackground = highlight_dark_color)
                            
                    self.possible_moves = moves
                    self.chosen_piece_position = coords

        else:
            if coords not in self.possible_moves:
                if self.gameboard[coords[0]][coords[1]].startswith(self.turn) and coords != self.chosen_piece_position:
                    self.render_board(self.turn)
                    
                    moves = logic.rules.get_legal_moves(self.gameboard, self.turn, coords, self.last_move_positions)
                    if len(moves) > 0:
                        self.phase = "choose_move"
                    
                        if (info["row"] % 2 == 0 and info["column"] % 2 == 0) or (info["row"] % 2 == 1 and info["column"] % 2 == 1):
                            self.gameboard_buttons[info["row"]][info["column"]].config(bg = highlight_light_color, activebackground = highlight_light_color)
                        else:
                            self.gameboard_buttons[info["row"]][info["column"]].config(bg = highlight_dark_color, activebackground = highlight_dark_color)
                        
                        for move in moves:
                            if self.turn == "w":
                                button_coords = (7 - move[0], move[1])
                            else:
                                button_coords = (move[0], 7 - move[1])
                            
                            if (button_coords[0] % 2 == 0 and button_coords[1] % 2 == 0) or (button_coords[0] % 2 == 1 and button_coords[1] % 2 == 1):
                                self.gameboard_buttons[button_coords[0]][button_coords[1]].config(bg = highlight_light_color, activebackground = highlight_light_color)
                            else:
                                self.gameboard_buttons[button_coords[0]][button_coords[1]].config(bg = highlight_dark_color, activebackground = highlight_dark_color)
                            
                        self.possible_moves = moves
                        self.chosen_piece_position = coords

                else:
                    self.phase = "pick_piece"
                    self.chosen_piece_position = (-1, -1)
                    self.possible_moves = []
                    self.render_board(self.turn)
                
            else:
                piece = self.gameboard[self.chosen_piece_position[0]][self.chosen_piece_position[1]]
                self.gameboard[self.chosen_piece_position[0]][self.chosen_piece_position[1]] = ""
                self.gameboard[coords[0]][coords[1]] = piece

                self.last_move_positions = (self.chosen_piece_position, coords)
                self.phase = "pick_piece"
                self.chosen_piece_position = (-1, -1)
                self.possible_moves = []

                if self.turn == "w":
                    self.turn = "b"
                else:
                    self.turn = "w"

                self.render_board(self.turn)

                game_over, winner = logic.rules.check_for_game_over(self.gameboard, self.turn, self.last_move_positions)
                if game_over:
                    self.announce_game_over(winner)
        

    def init_images(self):
        wk_image = Image.open("./images/pieces/wk.png")
        wk_image = wk_image.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
        self.wk_image = ImageTk.PhotoImage(wk_image, master = self.root)

        wq_image = Image.open("./images/pieces/wq.png")
        wq_image = wq_image.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
        self.wq_image = ImageTk.PhotoImage(wq_image, master = self.root)

        wb_image = Image.open("./images/pieces/wb.png")
        wb_image = wb_image.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
        self.wb_image = ImageTk.PhotoImage(wb_image, master = self.root)

        wn_image = Image.open("./images/pieces/wn.png")
        wn_image = wn_image.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
        self.wn_image = ImageTk.PhotoImage(wn_image, master = self.root)

        wr_image = Image.open("./images/pieces/wr.png")
        wr_image = wr_image.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
        self.wr_image = ImageTk.PhotoImage(wr_image, master = self.root)

        wp_image = Image.open("./images/pieces/wp.png")
        wp_image = wp_image.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
        self.wp_image = ImageTk.PhotoImage(wp_image, master = self.root)

        bk_image = Image.open("./images/pieces/bk.png")
        bk_image = bk_image.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
        self.bk_image = ImageTk.PhotoImage(bk_image, master = self.root)

        bq_image = Image.open("./images/pieces/bq.png")
        bq_image = bq_image.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
        self.bq_image = ImageTk.PhotoImage(bq_image, master = self.root)

        bb_image = Image.open("./images/pieces/bb.png")
        bb_image = bb_image.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
        self.bb_image = ImageTk.PhotoImage(bb_image, master = self.root)

        bn_image = Image.open("./images/pieces/bn.png")
        bn_image = bn_image.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
        self.bn_image = ImageTk.PhotoImage(bn_image, master = self.root)

        br_image = Image.open("./images/pieces/br.png")
        br_image = br_image.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
        self.br_image = ImageTk.PhotoImage(br_image, master = self.root)

        bp_image = Image.open("./images/pieces/bp.png")
        bp_image = bp_image.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
        self.bp_image = ImageTk.PhotoImage(bp_image, master = self.root)

        self.empty_image = tkinter.PhotoImage(width = tile_size, height = tile_size, master = self.root)


    def render_board(self, for_player):
        for i in range(8):
            for j in range(8):
                gameboard_space = ""
                if for_player == "w":
                    gameboard_space = self.gameboard[7-i][j]
                else:
                    gameboard_space = self.gameboard[i][7-j]
                    
                if gameboard_space == "":
                    self.gameboard_buttons[i][j].config(image = self.empty_image)
                elif gameboard_space == "wk":
                    self.gameboard_buttons[i][j].config(image = self.wk_image)
                elif gameboard_space == "wq":
                    self.gameboard_buttons[i][j].config(image = self.wq_image)
                elif gameboard_space == "wb":
                    self.gameboard_buttons[i][j].config(image = self.wb_image)
                elif gameboard_space == "wn":
                    self.gameboard_buttons[i][j].config(image = self.wn_image)
                elif gameboard_space == "wr":
                    self.gameboard_buttons[i][j].config(image = self.wr_image)
                elif gameboard_space == "wp":
                    self.gameboard_buttons[i][j].config(image = self.wp_image)
                elif gameboard_space == "bk":
                    self.gameboard_buttons[i][j].config(image = self.bk_image)
                elif gameboard_space == "bq":
                    self.gameboard_buttons[i][j].config(image = self.bq_image)
                elif gameboard_space == "bb":
                    self.gameboard_buttons[i][j].config(image = self.bb_image)
                elif gameboard_space == "bn":
                    self.gameboard_buttons[i][j].config(image = self.bn_image)
                elif gameboard_space == "br":
                    self.gameboard_buttons[i][j].config(image = self.br_image)
                elif gameboard_space == "bp":
                    self.gameboard_buttons[i][j].config(image = self.bp_image)

                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                    self.gameboard_buttons[i][j].config(bg = light_color, activebackground = light_color)
                else:
                    self.gameboard_buttons[i][j].config(bg = dark_color, activebackground = dark_color)


    def announce_game_over(self, winner):
        if winner == "w":
            message = "White player wins!"
        elif winner == "b":
            message = "Black player wins!"
        else:
            message = "Stalemate!"

        self.messagebox = tkinter.Tk()
        self.messagebox.title("Chess")
        self.messagebox.geometry("300x100")

        self.message_label = tkinter.Label(self.messagebox, text = message, font = ('Cantarell', 18))
        self.quit_btn = tkinter.Button(self.messagebox, text = "Quit", font = ('Cantarell', 18), command = self.quit)
        
        self.message_label.pack(pady = 10)
        self.quit_btn.pack(fill = 'x')

        self.messagebox.mainloop()

    def quit(self):
        self.root.destroy()
        self.messagebox.destroy()
