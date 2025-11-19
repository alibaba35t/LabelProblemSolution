import os
import pandas as pd

df = pd.read_csv("labels.csv")
df['subset'] = ""


length = int(len(df))
root_name = "/home/aliemre/Downloads/archive/archive (3)"
for i in range(0,length):
    file_name = str(df["pth"][i]).split("/")[1]
    for root, dirs, files in os.walk(root_name):
        if file_name in files:
            subset_name = os.path.basename(os.path.dirname(root))
            df.at[i, "subset"] = subset_name
            print(subset_name)
df.to_csv("new_labels.csv", index= False)
print(df.columns)
