import math


def Problem6_1(S):
    n = len(S)
    i = 1
    opt = [0] * n
    opt[0] = S[0]

    while i < n:
        opt[i] = max(opt[i-1] + S[i], S[i])
        i+=1;

    bestSum = max(opt)
    bestInd = opt.index(bestSum)

    tempSum = 0
    currInd = bestInd
    bestSeq = []
    while tempSum != bestSum:
        tempSum += S[currInd]
        bestSeq.append(S[currInd])
        currInd-=1

    bestSeq.reverse()

    print ("Input list: " + str(S))
    print("Best sum = " + str(bestSum))
    print("Best sequence = " + str(bestSeq))
    print("---------------------------------------")

if __name__ == '__main__':
    list = [5,15,-30,10,-5,40,10]
    Problem6_1(list)
    list = [1,2,3,4,5,6,7,8,9,10]
    Problem6_1(list)
    list = [-1,2,-3,4,-5,6,7,-8,9,10]
    Problem6_1(list)


