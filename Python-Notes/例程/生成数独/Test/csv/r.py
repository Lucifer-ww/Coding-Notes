import csv
f=open("data.csv",'r+')
c = csv.writer(f)
mm=[[1,, 'f'],[3,4],[5,6],[7,8],[9,0]]
c.writerow(mm[0])
f.close()