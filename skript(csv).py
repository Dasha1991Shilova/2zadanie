import pandas as pd
import csv
#pd.options.display.max_rows=2
#df = pd.read_csv('data.csv')
#strr = df.to_string()
#print(strr)
#print(df.head(1))
#print(df.tail(2))
#print(df.info())
with open('data.csv', 'r') as f:  
    data = csv.reader(f, delimiter=',')
    for row in data:
     print(row)
with open('data.csv', 'r') as f:  
    data = csv.DictReader(f, delimiter=',')
    for row in data:
     print(row)
with open('data.csv', 'r') as f:
    # читаем первые 100 символов (или весь файл)
    sample = f.read(100)    
    # пример проверки, что файл имеет заголовки
    header = csv.Sniffer().has_header(sample)
    print('В файле есть заголовки: ', header)
    # создаем диалект
    dialect = csv.Sniffer().sniff(sample)
with open('data.csv', 'r') as f:
    # передаем диалект и читаем файл
    reader = csv.reader(f, dialect)
    for row in reader:
        print(row)