import csv
with open('D:/PyCode/Demo/demo1415.csv', newline='') as csvfile:
   spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
   for row in spamreader:
      print(', '.join(row))
