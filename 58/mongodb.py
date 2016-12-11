import pymongo

client=pymongo.MongoClient('localhost,27017')
walden=client['walden']
sheet_line=walden['sheet_line']

path='/Users/dushibing/Desktop/walen.txt'

with open(path,'r') as f:
    lines=f.readlines()
    for index,line in enumerate(lines):
        data={
            'index':index,
            'line':line,
            'words':len(line.split())
        }
        sheet_line.insert_one(data)

