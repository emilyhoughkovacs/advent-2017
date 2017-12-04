import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_input():
  with open("inputday5.txt", "r") as f:
    return file.readlines()

def worker(row, pt2=False):
  # do work here
  # return a true or false if possible

def test():
  assert worker("test1") is True
  assert worker("test2") is True
  assert worker("test3") is True
  assert worker("test4") is True
  assert worker("test5", pt2=True) is True
  assert worker("test6", pt2=True) is True
  assert worker("test7", pt2=True) is True
  assert worker("test8", pt2=True) is True

def main():
  input = get_input()

  ## do work on each line of input here
  ## e.g. "how many rows of input are this"
  ## valid = sum([1 for row in input if isValid(row)])
  ## logger.info("Result: %s" % valid)

if __name__ == "__main__":
  if test():
    main()