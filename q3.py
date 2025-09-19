from collections import deque

def q3():
    try:
        n, m = map(int, input().split())  
        
        if not (4 <= n <= 200 and 4 <= m <= 200):
            print("N과 M은 4 이상 200 이하의 정수여야 합니다.")
            return
        
 
        emp = []
        for _ in range(n):
            row_input = input().strip()
            if len(row_input) != m:
                print(f"입력된 줄의 문자 개수가 M({m})개와 일치하지 않습니다.")
                return
            emp.append(row_input)            
    except (ValueError, IndexError):
        print("잘못된 입력입니다. 첫 줄에 두 숫자를, 다음 줄들에 0 또는 1로 구성된 문자열을 입력해주세요.")
        return


    graph = [list(map(int, row)) for row in emp]     
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    start = deque([(0, 0)]) 
    
    while start:  
        r, c = start.popleft()    
                                  
        for i in range(4):
            next_r, next_c = r + dr[i], c + dc[i]
            
            
            if 0 <= next_r < n and 0 <= next_c < m and graph[next_r][next_c] == 1:              
                graph[next_r][next_c] = graph[r][c] + 1
                start.append((next_r, next_c))
                
   
    print(graph[n-1][m-1])
    
q3()