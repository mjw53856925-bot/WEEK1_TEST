def q4():
    try:
       
        n, k = map(int, input().split())
        if not (1 <= n <= 100000 and 0 <= k <= n):
            print("N은 1 이상 100000 이하, K는 0 이상 N 이하의 정수여야 합니다.")
            return        
      
        a = list(map(int, input().split()))
        if len(a) != n:
            print("입력된 배열 A의 원소 개수가 N과 일치하지 않습니다.")
            return
            
        b = list(map(int, input().split()))
        if len(b) != n:
            print("입력된 배열 A의 원소 개수가 N과 일치하지 않습니다.")
            return
        
        for val in a + b:
            if not (1 <= val < 10000000):
                print("배열의 각 원소는 1 이상 10,000,000 미만의 자연수여야 합니다.")
                return
                
    except (ValueError, IndexError):
        print("잘못된 입력입니다. 입력 예시를 확인해주세요.")
        return
        
    a.sort()  
    b.sort(reverse=True) 
    
    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
            
    print(sum(a))
    
q4()