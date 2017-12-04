with open("inputday4.txt", "r") as f:
  rows = [x for x in f]
f.close()

valid = 0

def isValid(passphrase):
  passphrase = passphrase.split()
  newpp = []
  for word in passphrase:
    newpp.append(''.join(sorted(word)))
  if len(newpp)==len(set(newpp)):
    return True
  else:
    return False

for row in rows:
  if isValid(row):
    valid += 1

print valid

# print isValid("abcde fghij")
# print isValid("abcde xyz ecdab")
# print isValid("a ab abc abd abf abj")
# print isValid("iiii oiii ooii oooi oooo")
# print isValid("oiii ioii iioi iiio")