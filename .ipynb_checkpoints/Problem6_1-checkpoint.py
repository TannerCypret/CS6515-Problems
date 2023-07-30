import math


def Problem6_1(S):
    n = len(S)
    i = 1
    opt = [0] * n
    opt[0] = S[0]

    while i < n:
        opt[i] = max(opt[i-1] + S[i], S[i])
        print(str(opt[i]))
        i+=1;


    bestSum = max(opt)
    bestInd = opt.index(bestSum)

    tempSum = 0
    currInd = bestInd
    while tempSum != bestSum:
        tempSum += S[currInd]
        currInd-=1

    bs = bestSum     #Total sum of best sequence
    id = currInd + 1 #Start pos of best sequence

    print("best sum = " + str(bs))
    print("ID = " + str(id))


if __name__ == '__main__':
    list = [5,15,-30,10,-5,40,10]
    Problem6_1(list)

