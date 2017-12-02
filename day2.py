with open("inputday2.txt", "r") as f:
  rows = [x for x in f]
f.close()

checksum = 0

def diff(row):
  row = [int(num) for num in row.split()]
  diff = max(row)-min(row)
  return diff

def div(row):
  row = [float(num) for num in row.split()]
  for a in row:
    for b in row:
      if a!=b and a%b==0:
        return a/b

for row in rows:
  # print row
  # print [num for num in row.split()]
  checksum += div(row)
  # print len(row)==len(s)

# print div("3 8 6 5")

print checksum