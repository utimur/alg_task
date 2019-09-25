import csv
import json
import requests
import re

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    stroka = re.sub(r'((\w){1}\2+)',r'\2' ,line)
    print(stroka)








# arr =[]
# params = {
#     'json':True
# }
# with open('dataset_24476_3.txt','r') as file:
#     for line in file:
#         arr.append(line.strip())
# file = open('data.txt','a')
# for i in arr:
#
#     responce = requests.get('http://numbersapi.com/'+i +'/math',params=params)
#     value = responce.text
#     if(responce.json()['found'] == False):
#         file.writelines('Boring\n')
#     else:
#         file.writelines('Interesting\n')
# file.close()






# params={
#     'q':"Moscow",
#     'appid':'11c0d3dc6093f7442898ee49d2430d20',
#     'units':'Metric'
# }
# url = 'http://api.openweathermap.org/data/2.5/weather'
#
# responce = requests.get(url,params=params)
#
# print(responce)
# print(responce.headers['Content-type'])
# print(responce.json())
#
# data = responce.json()
#
# string = "Current temperature = {}"
# print(string.format(data['main']['temp']))
#



# student1= {'name':'Timur',
#            'surname':'Ulbi',
#             'mind':None}
# student2= {'name':'Timur',
#            'surname':'Ulbi',
#            'mind':True}
#
# arr = [student1,student2]
#
# print(json.dumps(arr,indent=4))
#

# count = 0
#
# dict = {}
# with open('Crimes.csv') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         dict[row[5]] = 0
# with open('Crimes.csv') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         value = dict.get(row[5])
#         value +=1
#         dict[row[5]] = value
#     print(dict)

