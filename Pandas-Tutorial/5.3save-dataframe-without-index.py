import pandas as pd

data = {
  "Name": ['A', 'B', 'C', 'D'],
  "roll_nu": [50, 40, 45, 20]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
df.to_csv(r'C:\Users\xpertji\Desktop\folder\filename.csv', index = False)
