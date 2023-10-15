#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)

def is_complete(board):
    """Checks if the Sudoku board is complete."""
    # Check if all cells are assigned
    for var in board:
        if board[var] == 0:
            return False  # There is at least one unassigned variable

    # Check if the board satisfies Sudoku constraints (no repeated values in rows, columns, and 3x3 boxes)
    for row in ROW:
        for col in COL:
            value = board[row + col]
            if not is_consistent(value, row + col, board):
                return False
    return True

def  select_unassigned_var(board):
    """"Selects an unassigned variable using the minimum remaining value heuristic."""
    unassigned_vars = []
    for var in board:
        if board[var] == 0:
            unassigned_vars.append(var)

        #remaining values for each unassigned variable
        remaining_values = {}
        for var in unassigned_vars:
            remaining_values[var] = 0
            for value in range(1, 10):
                if is_consistent(value, var, board):
                    remaining_values[var] += 1
        #select the unassigned variable with the smallest number of remaining values.
        min_val = min(remaining_values.values())
        selected_var = None
        for var in unassigned_vars:
            if remaining_values[var] == min_val:
                selected_var = var
                break
            return selected_var


def ordered_domain_values(var, board):
    """Returns a list of the values in the domain of the variable, sorted inascending order."""
    domain_values = []
    for value in range(1,10):
        if is_consistent(value, var, board):
            domain_values.append(value)
    domain_values.sort()
    return domain_values

def is_consistent(value, var, board):
    #check if the variable value is in the same row
    for var2 in board:
        print("Variable:", {var2}, "Value:", {board[var2]}) 
        if var2 != var and board[var2] == value and var2[0] == var[0]:
            return False
        
    #check if the variable value is in the same column
    for var2 in board:
        if var2 != var and board[var2] == value and var2[1] == var[1]:
            return False
        
    #check if the variable value is in the 3x3 grid
    row = var[0]
    col = var[1]
    row_start = ROW.index(row) // 3 * 3
    col_start = COL.index(col) // 3 * 3
    for var2 in board:
        var2_row = var2[0]
        var2_col = var2[1]
        var2_row_index = ROW.index(var2_row)
        var2_col_index = COL.index(var2_col)
        if var2 != var and board[var2] == value and var2_row_index >= row_start and var2_row_index < row_start + 3 and var2_col_index >= col_start and var2_col_index < col_start + 3:
            return False
    return True

def backtracking(board):
    """Takes a board and returns solved board."""
    if is_complete(board):
        solved_board = board
        return solved_board
    
    var = select_unassigned_var(board) # Uses minimum remaining value heuristic
    for value in ordered_domain_values(var, board):
        if is_consistent(value, var, board):
            board[var] = value
            solved_board = backtracking(board)
            if solved_board is not None:
                return solved_board
            board[var] = 0 # Removes the variable value from board
    return None # Returns failure board


if __name__ == '__main__':
    if len(sys.argv) > 1:
        
        # Running sudoku solver with one board $python3 sudoku.py <input_string>.
        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}       
        
        solved_board = backtracking(board)

        '''
        # Write board to file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        outfile.write(board_to_string(solved_board))
        outfile.write('\n') 


        for row in ROW:
            for col in COL:
                cell_name = row + col
                cell_value = board[cell_name]
                print(f"Value of cell {cell_name}: {cell_value}")

        '''

        print_board(board)

    else:
        # Running sudoku solver for boards in sudokus_start.txt $python3 sudoku.py

        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        # Setup output file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")

        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                      for r in range(9) for c in range(9)}
            
            # Print starting board. TODO: Comment this out when timing runs.
            print_board(board)

            # Solve with backtracking
            solved_board = backtracking(board)

            # Print solved board. TODO: Comment this out when timing runs.
            print_board(solved_board)

            # Write board to file
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')

        print("Finishing all boards in file.")