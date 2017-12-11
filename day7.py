import logging
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_input():
  with open("inputday7.txt", "r") as f:
    return f.readlines()

def splitLine(row):
  row = re.findall(r"[\w']+", row)
  node = row[0]
  val = int(row[1])
  if len(row) > 2:
    children = row[2:]
  else:
    children = []
  return node, val, children

# def worker(banks, pt2=False):

def test():
  # assert worker([0, 2, 7, 0]) == 6
  # assert worker("test6", pt2=True) is True
  # assert worker("test7", pt2=True) is True
  # assert worker("test8", pt2=True) is True
  return True

def main():
  input = get_input()
  myDict = {}
  weight = {}
  for row in input:
    x, y, z = splitLine(row)
    weight[x] = y
    myDict[x] = z
  roots = []
  leaves = []
  for a, b in myDict.iteritems():
    for c in b:
      leaves.append(c)
    roots.append(a)

  print [x for x in roots if x not in leaves]
  # roots = list(set(roots))
  # leaves = list(set(leaves))

  # for b in myDict.values():
  #   print b
  # print splitLine(input[3])
  # print myDict
  # input = [0, 2, 7, 0]

  ## do work on each line of input here
  ## e.g. "how many rows of input are this"
  ## valid = sum([1 for row in input if isValid(row)])
  ## logger.info("Result: %s" % valid)

if __name__ == "__main__":
  if test():
    main()