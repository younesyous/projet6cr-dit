import pandas as pd
import time

for n in range(0, 1):

    result = ""
    path1 = "G:/NetGuard_projet/aDoctor_NetGuard/doctor"+str(n)+".csv"
    path2 = "G:/NetGuard_projet/Organic_NetGuard/smells_csv_"+str(n)+".csv"
    a = pd.read_csv(path1)
    b = pd.read_csv(path2)

    merged = a.merge(b, on='Class')
    result = "result"+str(n)+".csv"
    merged.to_csv(result, index=False)

time.sleep(10)

for n in range(0, 1):
    result = "result"+str(n)+".csv"
    df = pd.read_csv(result)
    k = df.loc[~df.Class.duplicated(keep='last')]
    k.to_csv(result, index=False, na_rep='NaN')
