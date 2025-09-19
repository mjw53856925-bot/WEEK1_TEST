def q1():
    try:
        n = int(input())
        plan = input().split()
        
        if not (1 <= n <= 100):
            print("N은 1 이상 100 이하의 정수여야 합니다.")
            return
        if not (1 <= len(plan) <= 100):
            print("이동 횟수는 1 이상 100 이하의 정수여야 합니다.")
            return
            
    except (ValueError, IndexError):
        print("잘못된 입력입니다. 숫자를 입력하고, 다음 줄에 R, L, U, D 문자를 입력해주세요.")
        return

    x, y = 1, 1  
    
    moves = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    
    for move in plan:
        dx, dy = moves.get(move, (0, 0)) 
        next_x, next_y = x + dx, y + dy
        if 1 <= next_x <= n and 1 <= next_y <= n:
            x, y = next_x, next_y
            
    print(x, y)
    
q1()