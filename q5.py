def q5():
    try:      
        n, m = map(int, input().split())

        if not (1 <= n <= 1000000 and 1 <= m <= 2000000000):
            print("입력된 N 또는 M의 값이 유효한 범위를 벗어났습니다.")
            return
    
        heights = list(map(int, input().split()))
        
    except (ValueError, IndexError):
        print("잘못된 입력입니다. 입력 예시를 확인해주세요.")
        return
        
    start = 0          
    end = max(heights)  
    result = 0          
    
    while start <= end:
        mid = (start + end) // 2
       
        total_length = 0
        
        for height in heights:
            if height > mid:
                total_length += height - mid
       
        
        if total_length >= m:
            result = mid 
            start = mid + 1
      
        else:
            end = mid - 1
           
            
    print(result)
    
q5()