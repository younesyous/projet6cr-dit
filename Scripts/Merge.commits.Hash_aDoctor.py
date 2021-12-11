import csv
import os
import pandas as pd

CommitHash = pd.read_csv(
    r'G:/Gisapp_projet/CommitHash_gisapp.csv', sep=";")['CommitHash']
CommitDate = pd.read_csv(
    r'G:/Gisapp_projet/CommitHash_gisapp.csv', sep=";")['CommitDate']

os.chdir('G:/Gisapp_projet/doc_adoctor')
for i in range(0, 1):

    input = "G:/Gisapp_projet/gisapp_doc/doctor"+str(i)+".csv"
    output = "G:/Gisapp_projet/doc_adoctor/organicOut"+str(i)+".csv"

    with open(input, 'r') as csvinput:
        with open(output, 'w') as csvoutput:
            writer = csv.writer(csvoutput)
            for row in csv.reader(csvinput):
                writer.writerow([i]+[CommitHash[i]]+[CommitDate[i]]+row)

    file1 = pd.read_csv(output)
    headerList = ['Commit', 'CommitHash', 'CommitDate', 'Class', 'DTWC', 'DR', 'DW', 'IDFP', 'IDS', 'ISQLQ',
                  'IGS', 'LIC', 'LT', 'MIM', 'NLMR', 'PD', 'RAM', 'SL', 'UC']

    file1.to_csv("NewHead"+str(i)+".csv", header=headerList, index=False)
    file2 = pd.read_csv("NewHead"+str(i)+".csv")
