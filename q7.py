import sys

INF = int(1e9)  

def q7():
    try:
        n, m = map(int, input().split())

        if not (2 <= n <= 100 and 1 <= m <= 1000):
            print("N은 2 이상 100 이하, M은 1 이상 1000 이하의 정수여야 합니다.")
            return

        graph = [[INF] * (n + 1) for _ in range(n + 1)] 
        
       
        for i in range(1, n + 1):
            graph[i][i] = 0

        
        for _ in range(m):
            a, b = map(int, sys.stdin.readline().split()) 
           
            graph[a][b] = 1
            graph[b][a] = 1
            
        x, k = map(int, sys.stdin.readline().split())

    except (ValueError, IndexError):
        print("잘못된 입력입니다. 입력 예시를 확인해주세요.")
        return


    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for l in range(1, n + 1):
                graph[j][l] = min(graph[j][l], graph[j][i] + graph[i][l])

    distance = graph[1][x] + graph[x][k]

    if distance >= INF:
        print(-1)
    else:
        print(distance)
        
q7()