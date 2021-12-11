import csv
import os
import pandas as pd

CommitHash = pd.read_csv(
    r'G:/Gisapp_projet/CommitHash_gisapp.csv', sep=";")['CommitHash']
CommitDate = pd.read_csv(
    r'G:/Gisapp_projet/CommitHash_gisapp.csv', sep=";")['CommitDate']

os.chdir('G:/Gisapp_projet/Org_gissap')
for i in range(5, 1432):

    input = "G:/Gisapp_projet/gisapp_org/smells_csv_"+str(i)+".csv"
    output = "G:/Gisapp_projet/Org_gissap/organicOut"+str(i)+".csv"

    with open(input, 'r') as csvinput:
        with open(output, 'w') as csvoutput:
            writer = csv.writer(csvoutput)
            for row in csv.reader(csvinput):
                writer.writerow([i]+[CommitHash[i]]+[CommitDate[i]]+row)

    file1 = pd.read_csv(output)
    headerList = ['Commit', 'CommitHash', 'CommitDate', 'Class', 'LazyClass', 'ComplexClass', 'LongParameterList', 'FeatureEnvy', 'LongMethod', 'BlobClass',
                  'MessageChain', 'RefusedBequest', 'SpaghettiCode', 'SpeculativeGenerality']

    file1.to_csv("NewHead"+str(i)+".csv", header=headerList, index=False)
    file2 = pd.read_csv("NewHead"+str(i)+".csv")
