import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_input():
  with open("inputday5.txt", "r") as f:
    return f.readlines()

def worker(i, myList, pt2=False):
  if pt2 is True and myList[i] > 2:
    cur = i
    i = myList[i] + i
    myList[cur] -= 1
  else:
    cur = i
    i = myList[i]+i
    myList[cur] += 1
  return i, myList

def test():
  assert worker(0, [0, 3, 0, 1, -3]) == (0, [1, 3, 0, 1, -3])
  assert worker(0, [1,3,0 , 1 , -3]) == (1, [2,3,0 , 1 , -3])
  assert worker(1, [2, 3, 0 , 1 , -3]) == (4, [2, 4, 0, 1, -3])
  assert worker(4, [2, 4, 0, 1, -3]) == (1, [2, 4, 0, 1, -2])
  assert worker(1, [2, 4, 0, 1, -2]) == (5, [2, 5, 0, 1, -2])
  return True

def main():
  input = get_input()
  input = [int(x) for x in input]
  # input = [0, 3, 0, 1, -3]
  steps = 0
  index = 0
  while index in range(len(input)):
    index, input = worker(index, myList=input, pt2=True)
    steps += 1
    # print index

  print steps
  # print input

if __name__ == "__main__":
  if test():
    main()