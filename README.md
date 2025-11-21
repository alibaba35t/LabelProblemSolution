# LabelProblemSolution

[![Status: Training](https://img.shields.io/badge/Status-Active-green)](https://github.com/alibaba35t/ChallengeWithAffectnet)


I have been working on Facial Emotion Recognition (FER) models for a few days, and I chose the AffectNet dataset for facial expression classification. While examining the dataset, I noticed that the labels.csv file does not include any subset information (such as train or test), even though it contains more than 20,000 rows.

To address this issue, I wrote a script that automatically assigns a subset value to each row. The script determines whether a sample belongs to the train or test set by checking the base directory of the image file.

This ensures that every entry in labels.csv now includes a correct and consistent subset field, which makes data loading and model training much smoother.



## I faced with some Errors
- I downloaded affectnet in zip file format to my PC. Therefore, I fixed folder names(for instance, I saw an Anger folder in Test folder but in labels.csv, path names was written in lowercase). However, ın colab I download dataset everytime with kagglehub. This error raises every time when ı download.
- If ı use my custom dataloader some file paths haven't seen . Then I had to skip them (temporary solution).
- My first script (named main.py) was quite slow.
- After run process of new script, I found some files which have same name, same images but they placed in both Train and Test folders.(**DAMN**)



## Solutions and Update 
- I found a new method in Path library (which named ***rglob***) and I applied this method to make much safer and faster script. ***APPROVEDDDD!!!!!*** it is working faster.
- I improved my script but my repository is messy now. I have to organize.


### Targeted Updates
- Adding new implementations like MySQL integration( for example, table to csv file or dataframe)
- Organizing the scripts to become a pypl library
