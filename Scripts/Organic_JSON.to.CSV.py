import os
import shlex
import subprocess
import json
from collections import Counter
import json
import csv
import time

all_smells = ['LazyClass', 'ComplexClass', 'LongParameterList', 'FeatureEnvy', 'LongMethod',
              'BlobClass', 'MessageChain', 'RefusedBequest', 'SpaghettiCode', 'SpeculativeGenerality']
my_map = {}
# Set the environment variable
ECLIPSE_PATH = 'E://eclipse//plugins'
EQUINOX = ECLIPSE_PATH+'//org.eclipse.equinox.launcher_1.3.100.v20150511-1540.jar'
MAIN = 'org.eclipse.core.launcher.Main'
ORGANIC = 'organic.Organic'
path = 'G://Magisk'

for i in range(0, 1):
    list = []
    for n in range(i, i+1):

        path1 = path+"//"+str(n)
        # print(n)
        outversion = "G://organicSmells//"+"smells_json_0"+str(n)+".json"
        commande = 'java -jar -XX:MaxPermSize=2560m -Xms40m -Xmx2500m "%s" %s \
                   -application %s -sf "%s" -src "%s"'
        commande = commande % (EQUINOX, MAIN, ORGANIC, outversion, path1)
        args = shlex.split(commande)
        p = subprocess.Popen(args)
        list.append(outversion)

    print(list)

    time.sleep(30)
    for elem in list:

        with open(elem) as f_json:
            json_data = json.load(f_json)

        for entry in json_data:
            my_map[entry["fullyQualifiedName"]] = []

            # adding all class smells
            for class_smell in entry["smells"]:
                my_map[entry["fullyQualifiedName"]].append(class_smell)

            # adding all methods smells
            for method in entry["methods"]:
                for method_smell in method["smells"]:
                    my_map[entry["fullyQualifiedName"]].append(method_smell)

    os.chdir('G://organicSmells//csv_smells')

    for x in range(i, i+1):
        output = "smells_csv_"+str(x)+".csv"
        with open(output, 'w', newline='') as f_output:
            csv_output = csv.DictWriter(f_output, fieldnames=[
                                        "Class", *all_smells], extrasaction='ignore', restval='0')
            csv_output.writeheader()

            for elem in my_map:
                smell_counts = Counter()
                smell_counts['Class'] = elem
                for smell in my_map[elem]:
                    smell_counts[smell["name"]] += 1
                csv_output.writerow(smell_counts)
