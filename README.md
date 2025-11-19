# LabelProblemSolution
I have been working on Facial Emotion Recognition (FER) models for a few days, and I chose the AffectNet dataset for facial expression classification. While examining the dataset, I noticed that the labels.csv file does not include any subset information (such as train or test), even though it contains more than 20,000 rows.

To address this issue, I wrote a script that automatically assigns a subset value to each row. The script determines whether a sample belongs to the train or test set by checking the base directory of the image file.

This ensures that every entry in labels.csv now includes a correct and consistent subset field, which makes data loading and model training much smoother.
