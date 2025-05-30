import pandas as pd

train_dataset = pd.read_csv("files/output/train_dataset.csv", sep=",")
    
print(train_dataset.columns)
print(train_dataset.shape)
assert "phrase" in train_dataset.columns
assert "target" in train_dataset.columns

counts = train_dataset["target"].value_counts()

# assert counts["neutral"] == 1117

print(counts["neutral"])