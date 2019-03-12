# Exercise Address https://www.acmicpc.net/problem/14890
import sys

class pathWay():
    def comparisonColumn(self):
        countColumn = 0
        for i in range(roadLength):
            slopePossible = True
            for j in range(roadLength-1):
                if(Matrix[i][j] == Matrix[i][j+1]):
                    continue
                elif(abs(Matrix[i][j] - Matrix[i][j+1]) > 1):
                    slopePossible = False
                    break

                elif(Matrix[i][j] < Matrix[i][j+1]):
                    if(j+1-slopeLength >= 0 and slopeCheckMatrix[i][j+1-slopeLength] != 1):
                        for k in range(0, slopeLength):
                            if(j-k >= 0 and Matrix[i][j] == Matrix[i][j-k]):
                                slopeCheckMatrix[i][j-k] = 1
                            else:
                                slopePossible = False
                                break
                    else:
                        slopePossible = False
                        break

                elif(Matrix[i][j] > Matrix[i][j+1]):
                    for k in range(0, slopeLength):
                        if(j+1+k < roadLength and Matrix[i][j+1] == Matrix[i][j+1+k]):
                            slopeCheckMatrix[i][j+1+k] = 1
                        else:
                            slopePossible = False
                            break

            if(slopePossible):
                countColumn = countColumn + 1
        return countColumn

    def comparisonRow(self):
        countRow = 0
        for i in range(roadLength):
            slopePossible = True
            for j in range(roadLength-1):
                if(Matrix[j][i] == Matrix[j+1][i]):
                    continue
                elif(abs(Matrix[j][i] - Matrix[j+1][i]) > 1):
                    slopePossible = False
                    break

                elif(Matrix[j][i] < Matrix[j+1][i]):
                    if(j+1-slopeLength >= 0 and slopeCheckMatrix[j+1-slopeLength][i] != 1):
                        for k in range(0, slopeLength):
                            if(j-k >= 0 and Matrix[j][i] == Matrix[j-k][i]):
                                slopeCheckMatrix[j-k][i] = 1
                            else:
                                slopePossible = False
                                break
                    else:
                        slopePossible = False
                        break

                elif(Matrix[j][i] > Matrix[j+1][i]):
                    for k in range(0, slopeLength):
                        if(j+1+k < roadLength and Matrix[j+1][i] == Matrix[j+1+k][i]):
                            slopeCheckMatrix[j+1+k][i] = 1
                        else:
                            slopePossible = False
                            break

            if(slopePossible):
                countRow = countRow + 1
        return countRow

if __name__ == "__main__":

    wayCount = 0
    array = list(map(int, input().split()))

    roadLength = array[0]
    slopeLength = array[1]

    if(roadLength < 2 or roadLength > 100):
        print('행렬의 범위를 알맞게 입력해주세요')
        sys.exit(1)
    elif(slopeLength < 1 or slopeLength > roadLength):
        print('경사로의 길이를 알맞게 입력해주세요')
        sys.exit(1)

    Matrix = [list(map(int, input().split())) for i in range(roadLength)]

    pw = pathWay()
    slopeCheckMatrix = [[0]*roadLength for i in range(roadLength)]
    wayCount += pw.comparisonColumn()
    slopeCheckMatrix = [[0]*roadLength for i in range(roadLength)]
    wayCount += pw.comparisonRow()
    print(wayCount)
