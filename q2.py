def dfs(graph, x, y, n, m):
   
   
    if x < 0 or x >= n or y < 0 or y >= m or graph[x][y] == '1':
        return False
    
    if graph[x][y] == '0':
        graph[x][y] = '1'  
        dfs(graph, x - 1, y, n, m)
        dfs(graph, x + 1, y, n, m)
        dfs(graph, x, y - 1, n, m)
        dfs(graph, x, y + 1, n, m)
        return True 
    


def q2():
    
    try:
        n, m = map(int, input().split())
        
        if not (1 <= n <= 1000 and 1 <= m <= 1000):
            print("N과 M은 1 이상 1,000 이하의 정수여야 합니다.")
            return
            
        emp = []
        for _ in range(n):
            row_input = input()           
            if len(row_input) != m:
                print(f"입력된 줄의 문자 개수가 M({m})개와 일치하지 않습니다.")
                return
            emp.append(row_input)
            
    except (ValueError, IndexError):
        print("잘못된 입력입니다. 첫 줄에 두 숫자를, 다음 줄들에 0 또는 1로 구성된 문자열을 입력해주세요.")
        return
   
    
    graph = [list(row) for row in emp]
   

    ice_creams = 0
    for i in range(n):
        for j in range(m):
            if dfs(graph, i, j, n, m) == True:
                ice_creams += 1
                
    print(ice_creams)


q2()
