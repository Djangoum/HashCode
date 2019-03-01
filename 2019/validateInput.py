from collections import namedtuple

Image = namedtuple("Image", "id ori tagN tags")
Slide = namedtuple("Slide", "id1 id2 tagN tags")

def getImages(path):
  with open(path) as f:
    lines = f.readlines()
  print(len(lines))
  
  images = []
  lines = lines[1:]
  for i in range(len(lines)):
    images.append(getImage(i, lines[i]))
  return images

def getImage(index, line):
  row = line.strip().split(' ')
  return Image(index, row[0], row[1], row[2:])

def score_transition(slide1, slide2):
    common = len(list(set(slide1).intersection(slide2)))
    not_in_slide1 = len([x for x in slide1 if x not in slide2])
    not_in_slide2 = len([x for x in slide2 if x not in slide1])
    return min(common, not_in_slide1, not_in_slide2)  

file = "b_lovely_landscapes.txt"
images = getImages(file)
print(len(images))

with open("RandomSolution.txt") as f:
  lines = f.readlines()

lines.pop(0)
total = 0

for i in range(len(lines) - 1):
    idsLeft = lines[i].split(' ')
    idsRight = lines[i + 1].split(' ')
    if len(idsLeft) == 1 and len(idsRight) == 1:
        tran = score_transition(images[int(idsLeft[0])].tags, images[int(idsRight[0])].tags)
    elif len(idsLeft) == 1:
        vTags = set(images[int(idsRight[0])].tags + images[int(idsRight[1])].tags)
        tran = score_transition(images[int(idsLeft[0])].tags, vTags)
    elif len(idsRight) == 1:
        vTags = set(images[int(idsLeft[0])].tags + images[int(idsLeft[1])].tags)
        tran = score_transition(images[int(idsRight[0])].tags, vTags)
    else:
        vTagsLeft = set(images[int(idsLeft[0])].tags + images[int(idsLeft[1])].tags)
        vTagsRigth = set(images[int(idsRight[0])].tags + images[int(idsRight[1])].tags)
        tran = score_transition(vTagsLeft, vTagsRigth)
    total += tran

print(total)