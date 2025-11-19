import os
import pandas as pd

# 1. open csv file in dataframe format with pandas
df = pd.read_csv("labels.csv")
# 2. add new column named "subset"
df['subset'] = ""


length = int(len(df))

# Choose base directory of Train and Test directories
root_name = "/home/aliemre/Downloads/archive/archive (3)"

for i in range(0,length):
    # We scan folders for each image and in labels.csv "pth" columns format is "anger/image0000006.jpg" like that
    # You can change split method according to your file name
    file_name = str(df["pth"][i]).split("/")[1]
    
    for root, dirs, files in os.walk(root_name):
        if file_name in files:
            # In this dataset, paths like " Test/ anger/ image000000.jpg" 
            # My purpose was find "Test" or "Train" folder 
            subset_name = os.path.basename(os.path.dirname(root))
            # Write folder name under the subset column
            df.at[i, "subset"] = subset_name
            # for control
            print(subset_name)
# Apply changes to csv file             
df.to_csv("new_labels.csv", index= False)

