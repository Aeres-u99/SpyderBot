import modules.retriever as ret
import csv 
links = []
with open("url_list.csv","rt") as f:
    data = csv.reader(f)
    
    for row in data:
        print(row)
        links.append(row[0])

print(links)
i = ""
j = ' '
while(i in links):
    links.remove(i)

print(links)

retrieved_content = []

query = input("Enter the query:")

if len(query)>0:
    for i in links:
        out = ret.retrieve(i,query,False,False)
        retrieved_content.append(out)

print(retrieved_content)
