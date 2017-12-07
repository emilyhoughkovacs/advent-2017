import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_input():
  with open("inputday6.txt", "r") as f:
    blah = [x.split() for x in f][0]
    return [int(x) for x in blah]

def worker(banks, pt2=False):
  most = max(banks)
  i = banks.index(most)
  dist = len(banks)-i
  banks[i] = 0
  j = i
  for j in range(i+1, most+i+1):
    banks[j % len(banks)] += 1
  return banks

def test():
  # assert worker([0, 2, 7, 0]) == 6
  assert worker([0, 2, 7, 0]) == [2, 4, 1, 2]
  assert worker([3, 1, 2, 3]) == [0, 2, 3, 4]
  assert worker([4, 1, 2, 3]) == [1, 2, 3, 4]
  assert worker([3, 1, 2, 3]) == [0, 2, 3, 4]
  assert worker([0, 2, 3, 4]) == [1, 3, 4, 1]
  assert worker([1, 3, 4, 1]) == [2, 4, 1, 2]
  # assert worker("test6", pt2=True) is True
  # assert worker("test7", pt2=True) is True
  # assert worker("test8", pt2=True) is True
  return True

def main():
  input = get_input()
  # input = [0, 2, 7, 0]
  seen = []
  while input not in seen:
    seen.append(input[:])
    input = worker(input)
  print len(seen)-seen.index(input)

  ## do work on each line of input here
  ## e.g. "how many rows of input are this"
  ## valid = sum([1 for row in input if isValid(row)])
  ## logger.info("Result: %s" % valid)

if __name__ == "__main__":
  if test():
    main()