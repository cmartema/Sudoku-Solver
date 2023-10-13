# Sudoku Solver (coms4701-hw2)

Please read all the sections carefully:

## I. Introduction

The objective of Sudoku is to fill a 9x9 grid with the numbers 1-9 so that each column, row, and 3x3 sub-grid (or box) contains one of each digit. You may try out the game here: [sudoku.com](https://www.sudoku.com/). Sudoku has 81 variables, i.e. 81 tiles. The variables are named by row and column, and are valued from 1 to 9 subject to the constraints that no two cells in the same row, column, or box may be the same.

Frame your problem in terms of variables, domains, and constraints. We suggest representing a Sudoku board with a Python dictionary, where each key is a variable name based on location, and the value of the tile placed there. Using variable names A1... A9... I1... I9, the board above has:

- `sudoku dict["B1"] = 2`, and
- `sudoku dict["E2"] = 9`.

We give value zero to a tile that has not yet been filled.

## Executing your program

Your program will be executed as follows:

In the starter zip, `sudokus start.txt`, contains hundreds of sample unsolved Sudoku boards, and `sudokus finish.txt` contains the corresponding solutions. Each board is represented as a single line of text, starting from the top-left corner of the board, and listed left-to-right, top-to-bottom. If you place the file `sudokus start.txt` in the same folder as `sudoku.py`, the following command will apply your algorithm to all boards and produce an output. For detail, read the main method in the skeleton code.


The first board in `sudokus start.txt` is represented as the string:

0 0 3 0 2 0 6 0 0
9 0 0 3 0 5 0 0 1
0 0 1 8 0 6 4 0 0
0 0 8 1 0 2 9 0 0
7 0 0 0 0 0 0 0 8
0 0 6 7 0 8 2 0 0
0 0 2 6 0 9 5 0 0
8 0 0 2 0 3 0 0 9
0 0 5 0 1 0 3 0 0


Your program will generate `output.txt`, containing a single line of text representing the finished Sudoku board. E.g.:

483921657967345821251876493548132976729564138136798245372689514814253769695417382


Test your program using `sudokus finish.txt`, which contains the solved versions of all the same puzzles. All puzzles provided contain unique solutions.

## III. Backtracking Algorithm

Implement backtracking search using the minimum remaining value heuristic. Pick your order of values to try for each variable, and apply forward checking to reduce variable domains.

- Test your program on `sudokus start.txt`.
- Report the number of puzzles you can solve and the mean, standard deviation, min, and max of the runtime over all puzzles in `sudokus start.txt`.

## IV. Important Information

1. Test-Run Your Code: Test, test, test. Make sure you produce an output file with the exact format of the example given.

2. Grading Submissions: We test your final program on 20 boards. Each board is worth 5 points if solved, and zero otherwise. These boards are similar to those in your starter zip, so if you solve all those, you'll get full credit.

3. Time Limit: No brute-force! Your program should solve puzzles in well under a minute per board. Programs with much longer running times will be killed.

4. Just for fun: Try your code on the world's hardest Sudokus! There's nothing to submit here, just for fun. For example:

Sudoku:
800000000003600000070090200050007000000045700000100030001000068008500010090000400


Solution:
812753649943682175675491283154237896369845721287169534521974368438526917796318452


## IV. What You Need To Submit

1. Your `sudoku.py` file (and any other Python code dependency).
2. A `README.txt` with your results, including:
   - The number of boards you could solve from `sudokus start.txt`.
   - Running time statistics: min, max, mean, and standard deviation.

## V. Before You Submit

- Ensure that your file is named `sudoku.py`.
- Ensure that your file compiles and runs.
- After your submission on Gradescope, you will receive feedback in 5 minutes on whether your code has the proper filename, output format, and execution time. Please address any issues and resubmit before the deadline.








