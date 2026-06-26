DATASET CLEANING 
File: clean_dataset.py 
import pandas as pd 
 
df = pd.read_csv("gesture_dataset.csv") 
df = df.dropna().drop_duplicates() 
 
for i in range(1, 3): 
    df = df[(df[f"flex{i}"] >= 0) & (df[f"flex{i}"] <= 4095)] 
 
df = df[ 
    df["ax"].between(-2, 2) & 
    df["ay"].between(-2, 2) & 
    df["az"].between(-2, 2) & 
 
 
    df["gx"].between(-500, 500) & 
    df["gy"].between(-500, 500) & 
    df["gz"].between(-500, 500) 
] 
 
df["label"] = df["label"].str.upper().str.strip() 
 
sensor_cols = [ 
    "flex1","flex2", 
    "ax","ay","az", 
    "gx","gy","gz" 
] 
 
df[sensor_cols] = df.groupby("label")[sensor_cols].transform( 
    lambda x: x.rolling(5, min_periods=1).mean() 
) 
 
min_samples = df["label"].value_counts().min() 
df = df.groupby("label").sample(min_samples, random_state=42) 
 
df.to_csv("gesture_dataset_cleaned.csv", index=False) 
 
 
print("Dataset cleaned & saved")