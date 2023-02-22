import pandas as pd

csv = pd.read_csv("/Users/yuntaemin/Desktop/Project/NYSU/Video Cutting Python Program/metadata/UrbanSound8K.csv")

for i in range(500):
  loc = len(csv)

  csv.loc[loc] = [f"{i % 10 + 1}-{i // 10 + 1}.wav", None, None, None, None, i % 10 + 1, 11, "baby_crying"]

csv.to_csv("/Users/yuntaemin/Desktop/Project/NYSU/Video Cutting Python Program/metadata/UrbanSound8kUphand.csv", index=False)