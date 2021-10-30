import os
import glob

mypath = os.path.dirname(os.path.abspath(__file__))
filist = sorted(glob.iglob(mypath + "\\" + "*.ts"))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("out.ts", 'ab') as out:

    for fn in filist:
        # print(fn)

        with open(fn, 'rb') as fh:
            for data in fh:
                out.write(data)
