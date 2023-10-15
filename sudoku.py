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
    """Checks to see if there are any values removed."""
    for row in board:
        if 0 in row:
            return False  # There is at least one unassigned variable in rows

    for col in range(9):
        if any(board[row][col] == 0 for row in range(9)):
            return False  # There is at least one unassigned variable in columns

    # Check 3x3 boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            if any(board[row][col] == 0 for row in range(box_row, box_row + 3) for col in range(box_col, box_col + 3)):
                return False  # There is at least one unassigned variable in a 3x3 box
    return True
    
def  select_unassigned_var(board):
    """Chooses the unassigned variable with the smallest domain size (MRV)."""
    var = None
    min_domain = float('inf') #Sets it to infinity 
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                if domain_size((row, col), board) < min_domain:
                    var = (row, col)
                    min_domain = domain_size(var, board)
    return var


def ordered_domain_values():
    pass
def is_consistent():
    pass

def domain_size(var, board):
    """Returns the size of the domain for the variable"""
    if board[var[0]][var[1]] != 0:
        return 1
    else:
        valid_values = set(range(1, 10)) 
        row, col = var
        #Check row
        for i in range(9):
            value = board[row][i]
            if value in valid_values:
                valid_values.remove(value)
        #Check column
        for i in range(9):
            value = board[i][col]
            if value in valid_values:
                valid_values.remove(value)
        #Check the 3x3 
        box_row, box_col = (row // 3) * 3, (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                value = board[i][j]
                if value in valid_values:
                    valid_values.remove(value)

        return len(valid_values)


def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    failure = board
    if is_complete(board):
        solved_board = board
        return solved_board
    
    var = select_unassigned_var(board) # Uses minimum remaining value heuristic
    for value in ordered_domain_values(var, board):
        if is_consistent(value, var, board):
            board[var[0]][var[1]] = value
            solved_board = backtracking(board)
            if solved_board != failure:
                return solved_board
            board[var[0]][var[1]] = 0 # Removes the variable value from board
    return failure # Returns failure board


if __name__ == '__main__':
    if len(sys.argv) > 1:
        
        # Running sudoku solver with one board $python3 sudoku.py <input_string>.
        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}       
        '''
        solved_board = backtracking(board)
        
        # Write board to file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        outfile.write(board_to_string(solved_board))
        outfile.write('\n') 

        '''
        
        for row in "ABCDEFGHI":
            for col in "123456789":
                cell_name = row + col
                cell_value = board[cell_name]
                print(f"Value of cell {cell_name}: {cell_value}")

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