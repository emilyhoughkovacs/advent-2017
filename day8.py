import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

c = {
   '==': lambda x,y: x == y,
   '!=': lambda x,y: x != y,
   '<': lambda x,y: x<y,
   '<=': lambda x,y: x<=y,
   '>': lambda x,y: x>y,
   '>=': lambda x,y: x>=y,
   'inc': lambda x,y: x+y,
   'dec': lambda x,y: x-y
}

def get_input():
  with open("inputday8.txt", "r") as f:
  # with open("test.txt", "r") as f:
    return f.readlines()

def splitLine(row):
  row = row.split() 
  var = row[0]
  sign = row[1]
  amt = row[2]
  d = row[4]
  compare = row[5]
  val = row[6]
  return var, sign, int(amt), d, compare, int(val)

def worker(row, theDict, pt2=False):
  var, sign, amt, d, compare, val = splitLine(row)
  if c[compare](theDict[d], val):
    theDict[var] = c[sign](theDict[var], amt)
  return theDict

def test():
  return True

def main():
  input = get_input()
  input = [x for x in input]
  myDict = {x.split()[0]:0 for x in input}
  most = 0

  for row in input:
    myDict = worker(row, myDict)
    if max(myDict.values()) > most:
      most = max(myDict.values())
  print most

if __name__ == "__main__":
  if test():
    main()