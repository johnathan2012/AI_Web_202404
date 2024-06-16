#讀取csv檔案
import csv

#先讀取csv檔案
with open('../Demo/demo1415.csv', 'r',
          encoding = 'utf-8') as fino:
    
   #將讀取的csv檔案寫入另一個檔案
   with open('demo107.txt', 'w',
              encoding = 'utf-8') as fouto:
        
      reader_csv = csv.reader(fino)
      write_txt = csv.writer(fouto)        
      for row in reader_csv:            
         print(', '.join(row))
         write_txt.writerow(row)
