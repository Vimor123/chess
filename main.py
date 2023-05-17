import tkinter

root = tkinter.Tk()
root.title("Chess")
root.geometry("800x800")

title_label = tkinter.Label(root, text = "Chess", font = ('Cantarell', 18))
play_btn = tkinter.Button(root, text = "Play", font = ('Cantarell', 18))
exit_btn = tkinter.Button(root, text = "Exit", font = ('Cantarell', 18))

title_label.grid(row = 0, column = 0, sticky = tkinter.W + tkinter.E)
play_btn.grid(row = 1, column = 0, sticky = tkinter.W + tkinter.E)
exit_btn.grid(row = 2, column = 0, sticky = tkinter.W + tkinter.E)

root.mainloop()
