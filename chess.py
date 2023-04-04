import pandas as pd
import random

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('responses.csv')

# Shuffle the rows randomly
df = df.sample(frac=1)

# Extract the user IDs as a list
user_ids = df['Chess.com User ID'].tolist()
print("")
print("Total number of participants:",len(user_ids))
print("\n")

# Make sure there are an even number of user IDs
if len(user_ids) % 2 != 0:
    user_ids.append(None)

# Create pairs by pairing consecutive user IDs
pairs = [(user_ids[i], user_ids[i+1]) for i in range(0, len(user_ids), 2)]

# Print out the pairs
for pair in pairs:
    print(pair)
    print("")
