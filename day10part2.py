import sys
import os
from itertools import cycle
from functools import reduce

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday10.txt'
        f = open(file, 'r')
        sizes = [ord(x) for x in f.readline()]
        f.close()

        sizes+=[17, 31, 73, 47, 23]

        print(sizes)

        currentPosition = 0
        skipSize = 0
        myList = [x for x in range(256)]

        for n in range(64):
            for ix, x in enumerate(sizes):
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
                while currentPosition>len(myList):
                    currentPosition = currentPosition-len(myList)
                skipSize+=1
                # print('i, x:', ix, x)
                # print("i, currentPosition, skipSize:", ix, currentPosition, skipSize)
                # print("segment:", segment)
                # print(myList)
                # print("current position and skip size:", currentPosition, skipSize)

        bounds = [x for x in range(0, 256+16, 16)]

        newList = list()
        for i in range(len(bounds)-1):
            newList.append(reduce(lambda x, y: x^y, myList[bounds[i]:bounds[i+1]]))

        newList = ['0'+hex(x)[2:4] if len(hex(x)[2:4])==1 else hex(x)[2:4] for x in newList]
        return ''.join(newList)
        # return [hex(x)[2:4] for x in [64, 7, 255]]

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()