d = [0] * 91

def fibonacci(n):
    if d[n] != 0:
        return d[n]

    if n <= 1:
        return n

    d[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return d[n]

def q6():
    n = int(input())
    
    if not (0 <= n <= 90):
        print("n은 0 이상 90 이하의 정수여야 합니다.")
        return
    
    results = []
    for i in range(n + 1):
        results.append(str(fibonacci(i)))

    print(", ".join(results))

q6()