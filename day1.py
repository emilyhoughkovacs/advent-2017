from datetime import datetime

with open("inputday1.txt", "r") as f:
  text = str(f.read())
f.close()

test = "1212"

def getSum(code=test):
  theSum = 0

  code = [int(x) for x in list(code)]

  for x in range(len(code)-1):
    if code[x]==code[x+1]:
      theSum += code[x]

  if code[-1]==code[0]:
    theSum += code[-1]

  return theSum

def partTwo(code=test):
  theSum = 0
  mid = len(code)/2

  l1 = [int(x) for x in list(code)[0:mid]]
  l2 = [int(x) for x in list(code)[mid:]]

  for a, b in zip(l1, l2):
    if a==b:
      theSum += 2*a

  return theSum

# print len(text)
# print getSum(text)

print str(datetime.now())
print partTwo(text)
print str(datetime.now())