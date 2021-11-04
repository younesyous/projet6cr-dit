import os
import shlex
import subprocess

os.chdir('C:/Users/Younes/Desktop/aDoctor')

path = 'G:/NetGuard_clone'

for n in range(0, 1):

    path1 = path+"/"+str(n)
    print(path1)
    outversion = "G:/doc_netguard/"+"doctor"+str(n)+".csv"
    cmd = 'java -cp aDoctor-1.0.jar it.unisa.aDoctor.process.RunAndroidSmellDetection %s %s "111111111111111"'
    cmd = cmd % (path1, outversion)
    args = shlex.split(cmd)
    p = subprocess.Popen(args)
