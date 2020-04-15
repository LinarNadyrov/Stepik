import requests

with open('dataset_3378_2.txt') as inf:
    r = requests.get(inf.readline().strip())
    print(len(r.text.splitlines()))
