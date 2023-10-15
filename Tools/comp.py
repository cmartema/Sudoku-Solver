def compare_files(file1, file2):
    '''reads the lines of both files, compares them, and prints "Success" for matching lines and "Failure" for non-matching lines. 
        If the number of lines in the files doesn't match, it prints a failure message as well'''
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        if len(lines1) != len(lines2):
            print("Failure: Number of lines in the files doesn't match.")
            return

        for line_num, (line1, line2) in enumerate(zip(lines1, lines2)):
            if line1 == line2:
                print(f"Success: Line {line_num + 1} matches.")
            else:
                print(f"Failure: Line {line_num + 1} does not match.")

file1 = 'output.txt'
file2 = 'sudokus_finish.txt'
compare_files(file1, file2)