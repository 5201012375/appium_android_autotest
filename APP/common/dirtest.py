import os


# curdir = os.getcwd()
# sp = os.path.split(curdir)
# print(sp)
# reportdir = os.path.join(sp[0],"report")
# print(reportdir)
uperdir = os.path.split(os.getcwd())
curdir = os.path.abspath(__file__)
print(curdir)
print(uperdir)
minedir = os.path.join(uperdir[0],uperdir[1],"APP","common","mine.json")
print(minedir)
