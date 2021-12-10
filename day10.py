import sys
import os
from itertools import cycle

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday10.txt'
        f = open(file, 'r')
        sizes = [int(x) for x in f.readline().split(',')]
        f.close()

        currentPosition = 0
        skipSize = 0
        myList = [x for x in range(256)]

        # print(myList)

        for x in sizes:
            # print("myList: ", myList)
            segment = list()
            pool = cycle(myList[currentPosition:]+myList[:currentPosition])
            for i in range(x):
                segment.append(next(pool))
            segment = segment[::-1]
            for j in range(min(len(myList[currentPosition:]), len(segment))):
                myList[currentPosition+j] = segment[j]
            # print("checkpoint1:", myList)
            if len(segment)> len(myList[currentPosition:]):
                carry = len(segment)-len(myList[currentPosition:])
                # print("myList[:carry]:", myList[carry])
                # print("segment[-carry:]:", segment[-carry:])
                # print("carry:", carry)
                myList[:carry] = segment[-carry:]
            # print("checkpoint2:",myList)
            currentPosition = currentPosition+x+skipSize
            if currentPosition>len(myList):
                currentPosition = currentPosition-len(myList)
            skipSize+=1
            # print("segment:", segment)
            # print(myList)
            # print("current position and skip size:", currentPosition, skipSize)

        return myList[0]*myList[1]

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()