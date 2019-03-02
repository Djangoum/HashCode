import numpy as numpy
import pandas as pd

path = "b_lovely_landscapes.txt"

with open(path) as f:
    lines = f.readlines()
lines.pop(0)

data = {'id': [], 'ori': [], 'tagN':[], 'tags': []}

for i in range(len(lines)):
    splittedLine = lines[i].split(' ')
    data['id'].append(i)
    data['ori'].append(splittedLine[0])
    data['tagN'].append(int(splittedLine[1]))
    data['tags'].append(splittedLine[2:])

images = pd.DataFrame(data)

print(images.head(1))
print(images.tail(1))
print(sum(images['tagN']))
tags = {}

for i, image in images.iterrows():
    for tag in image.tags:
        if tag in tags:
            tags[tag] += 1
        else:
            tags[tag] = 1

print(len(tags.values()))
print(max(tags.values()))