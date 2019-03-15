# Exercise Address https://www.acmicpc.net/problem/11403
import sys
import queue

class Graph():

    def bfs(matrix, vertex):
        for i in range(vertex):
            for j in range(vertex):
                if(matrix[i][j] == 1):
                    qu.put(j)
            while(not qu.empty()):
                currentY = qu.get()
                for k in range(vertex):
                    if(matrix[currentY][k] == 1 and matrix[i][k] != 1):
                        matrix[i][k] = 1
                        qu.put(k)
            for j in range(vertex):
                print(str(matrix[i][j]) + " ", end='')
            print("")




if __name__ == "__main__":

    vertex = int(input())

    matrix = [list(map(int, input().split())) for i in range(vertex)]

    if(vertex > 100 or vertex < 1):
        print("정점의 개수가 잘못 입력되었습니다.")
        sys.exit(1)

    qu = queue.Queue()

    gr = Graph()
    Graph.bfs(matrix, vertex)
