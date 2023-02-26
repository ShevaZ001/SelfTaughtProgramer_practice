import csv

with open('./python_practice/9-1_madeCsvSampe01.csv','w',newline='') as f:
    w=csv.writer(f,delimiter=',')
    w.writerow(['Top Gun','Risky Business','Minority Report'])
    w.writerow(['Titanic','The Revenant','Inception'])
    w.writerow(['Training Day','Man on Fire','Flight'])

print('output is done!!')
