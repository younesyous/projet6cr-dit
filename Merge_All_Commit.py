import os
import pandas as pd

os.chdir('G://NetGuard_projet//Organic_NetGuard')

master_df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        master_df = master_df.append(pd.read_csv(file))

master_df.to_csv('Organic All_merge.csv', index=False)
