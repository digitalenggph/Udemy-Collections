import tkinter as tk
from tkinter import messagebox

class TicTacToeBoard(tk.Tk):
    def __init__(self, board_size=3):
        super().__init__()
        self.title("Let's play Tic-Tac-Toe!")
        self.minsize(width=300, height=300)
        self.config(padx=100, pady=100)

        # non-Tk
        self.board_size = board_size
        self.current_player = "X"
        self.grid_name = []
        self.winning_combination = {}
        self.button_dict = {}
        self.cell_filled = {}

        # name buttons in grid
        self.fill_grid_names(self.board_size)

        # make buttons
        self.make_buttons(self.grid_name)

        # generate winning combination
        self.get_winning_combination(self.board_size)

        # make reset button
        self.reset_button = tk.Button(text="Reset", command=self.reset, 
                                      height=3, width=5)
        self.reset_button.grid(row=board_size+1, column=0)

        # make exit button
        self.exit_button = tk.Button(text="Exit", command=self.close_game, 
                                      height=3, width=5)
        self.exit_button.grid(row=board_size+1, column=board_size-1)


    def fill_grid_names(self, board_size):
        for row in range(board_size):
            for col in range(board_size):
                self.grid_name.append(f"{row}_{col}")


    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def get_cell_grid(self):
        for name, button in self.button_dict.items():
            self.cell_filled[name] = button['text']


    def click_button(self, btn):
        if btn["text"] == '':
            btn["text"] = self.current_player

            self.get_cell_grid()
            btn["state"] = "disabled"
            if self.check_win() is None:
                self.switch_player()
            else:
                winner = self.check_win()
                self.disable_buttons()
                self.reset_button['text'] = 'Play Again!'
                messagebox.showinfo("showinfo", f"Player {winner} wins!") 

                

    def make_buttons(self, grid_name):
        for button_name in grid_name:
            self.button_dict[button_name] = tk.Button(self, text='', height=5, width=5)
            button_object = self.button_dict[button_name]
            row, col = button_name.split("_")
            button_object.grid(row=row,column=col)
            button_object.config(command=lambda b=button_object: self.click_button(b))


    def get_winning_combination(self, board_size):
        self.winning_combination, win_hor, win_ver = {}, [], []
        for row in range(board_size):
            win_hor_lines, win_ver_lines = [], []
            for col in range(board_size):
                win_hor_lines.append(f"{row}_{col}")
                win_ver_lines.append(f"{col}_{row}")
            win_hor.append(win_hor_lines)
            win_ver.append(win_ver_lines)
        
        win_dia = [[f"{x}_{x}" for x in range(board_size)], [f"{board_size-x-1}_{x}" for x in range(board_size)]]

        self.winning_combination['horizontal'] = win_hor
        self.winning_combination['vertical'] = win_ver
        self.winning_combination['diagonal'] = win_dia
        return self.winning_combination
    
    def check_win(self):
        winning_dict = self.winning_combination
        symbol_to_value = {'X': 1, 'O': -1, '': 0}
        current_grid = {k: symbol_to_value.get(v, 0) for k, v in self.cell_filled.items()}

        for directions, combination_list in winning_dict.items():
            for combination in combination_list:
                sum = 0
                for cell in combination:
                    sum += current_grid[cell]

                if sum == self.board_size * 1:
                    return 'X'

                if sum == self.board_size * -1:
                    return 'O'
                
        return None

    
    def reset(self):
        self.reset_button['text'] = 'Reset'
        self.current_player = 'X'
        for k, v in self.button_dict.items():
            v["state"] = "normal"
            v.config(text='')
            self.cell_filled[k] = ''


    def disable_buttons(self):
        for k, v in self.button_dict.items():
            v["state"] = "disabled"
   

    def close_game(self):
        self.destroy()



        # LONG-CUT

        # # check horizontal
        # for row in winning_dict['horizontal']:
        #     sum_row = 0
        #     for cell in row:
        #         sum_row += current_grid[cell]
        #         if sum_row == self.board_size * 1:
        #             print('X wins!')
                
        #         if sum_row == self.board_size * -1:
        #             print('O wins')

        
        # # check vertical
        # for column in winning_dict['vertical']:
        #     sum_column = 0
        #     for cell in column:
        #         sum_column += current_grid[cell]
        #         if sum_column == self.board_size * 1:
        #             print('X wins!')
                
        #         if sum_column == self.board_size * -1:
        #             print('O wins')
                
        
        # # check diagonal
        # for diagonal in winning_dict['diagonal']:
        #     sum_diagonal = 0
        #     for cell in diagonal:
        #         sum_diagonal += current_grid[cell]
        #         if sum_diagonal == self.board_size * 1:
        #             print('X wins!')
                
        #         if sum_diagonal == self.board_size * -1:
        #             print('O wins')



            





