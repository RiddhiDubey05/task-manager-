import tkinter as tk
from tkinter import messagebox
def check_winner():
    for combo in [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "" ;
            bottons[combo[0]].config(bg="green")
            bottons[combo[1]].config(bg="green")
            bottons[combo[2]].config(bg="green")
messagebox.showinfo("tic tac toe",f"Player{buttons [combo[0]]['text']} wins")
root.quit()

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toogle_player()

        def toogle_player():
             global current_player
             current_player = "x" if current_player == "o" else "o"
             label.config(text=f"Player {current_player}'s turn")

             root = tk.Tk()
             root.title("Tic-Tac-Toe")

             bottons = [tk.Botton(root, text="", font=("normal", 24), width=5, height=2, command=lambda i=i: botton_click(i)) for i in range(9)]
             for i, button in enumerate(buttons):
                    button.grid(row=i // 3, column=i % 3)

                    currnt_player = "x"
                    winner = False
                    label = tk.lable(root, text=f"player {current_player}'s turn", font=("normal", 16))
                    label.grid(row=3, column=0, columnspan=3)
                    root.mainloop()
                    
