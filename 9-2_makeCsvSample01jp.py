import csv

with open('./python_practice/9-2_madeCsvSampe01jp.csv','w',newline='') as f:
    w=csv.writer(f,delimiter=',')
    w.writerow(['とっぷがん','りすきぃびじねす','まいのりていれぽうと'])
    w.writerow(['たいたにっく','れべなんと','いんせぷしょん'])
    w.writerow(['とれいにんぐでい','まんおんふあいあ','ふらいと'])

print('output is done!!')
