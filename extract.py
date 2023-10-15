import pandas as pd
'''extract the board number and running time from your text output and create an Excel file (running_times.xlsx) with 
    two columns: "Board Number" and "Running Time (seconds)." '''
# Step 1: Copy the text output to a file, e.g., time_output.txt

# Step 2: Read the file and extract the values
filename = 'time.txt'
with open(filename, 'r') as file:
    lines = file.readlines()

data = []
for line in lines:
    if line.strip():  # Ignore empty lines
        parts = line.strip().split(': ')
        board_number = int(parts[0].split()[-1])
        running_time = float(parts[1].split()[0])
        data.append((board_number, running_time))

# Step 3: Create a DataFrame and export to Excel
df = pd.DataFrame(data, columns=['Board Number', 'Running Time (seconds)'])

# Export to an Excel file
excel_filename = 'running_times.xlsx'
df.to_excel(excel_filename, index=False)