import pandas as pd
import re

#Read the CSV file
csv_file = "london_houses - Copy.csv"
data = pd.read_csv(csv_file)

#Save the Data_Frame to a file
txt_file = "london_houses_copy.txt"
data.to_csv(txt_file,sep="\t",index=False)

print(f"CSV File '{csv_file}' has been successfully converted to TXT file '{txt_file}'.")

#file reading starts here
i = 1
with open(txt_file) as file:

    for e_line in file:
        print(f"{i} - {e_line}")