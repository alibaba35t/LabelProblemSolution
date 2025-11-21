import pandas as pd
import os
from pathlib import Path

df = pd.read_csv("new_labels_V2.csv")
df2 = pd.read_csv("new_labels.csv") # This dataframe for comparing the subset names

target_path= str(df["pth"][0]).split("/")[1]
df["subset"].astype(str)
miss_matched = 0

for img_pth in Path("/home/aliemre/Desktop/archive/archive (3)/").rglob("*.jpg"):
    path_to_pth = "/".join(str(img_pth).split("/")[-2:])
    path_to_subset = str(img_pth).split("/")[6]

    try:
        index = df.index[df["pth"] == path_to_pth].tolist()[0]
        index2 = df2.index[df["pth"] == path_to_pth].tolist()[0]
        if pd.isna(df.at[index,"subset"]) or df.at[index,"subset"] == "":
            df.at[index,"subset"] = path_to_subset
        #This section was built for how many files mis-matched
        if str(df.at[index, "subset"]) != str(df2.at[index2, "subset"]):
            print(repr(str(df.at[index, "subset"])),repr(str(df2.at[index2, "subset"])))
            miss_matched= miss_matched + 1
            print(str(miss_matched), str(index), str(index2))

    except IndexError:
        continue
df.to_csv("new_labels_V2.csv", index=False)

print("completed")