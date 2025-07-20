t = int(input())

for case in range(1,t+1):
    n = int(input())
    array = []

    for _ in range(n): # input 행렬
        a = list(map(int,input().split()))
        array.append(a)
   
        
    array_90 = [[]*n for _ in range(n)]
    for row in range(n-1,-1,-1):
        temp = array[row]
        for col in range(n):
            array_90[col].append(temp[col])
            
    array_180 = [[]*n for _ in range(n)]
    for row in range(n-1,-1,-1):
        temp = array_90[row]
        for col in range(n):
            array_180[col].append(temp[col])

    array_270 = [[]*n for _ in range(n)]
    for row in range(n-1,-1,-1):
        temp = array_180[row]
        for col in range(n):
            array_270[col].append(temp[col])

    res = [[]*n for _ in range(n)] # 최종 행렬
    temp90 = ''
    temp180 = ''
    temp270 = ''
    for row in range(n):
        for col in range(n):
            
            temp90 += str(array_90[row][col]) 
            temp180 += str(array_180[row][col])
            temp270 += str(array_270[row][col])
            
            if len(temp90) == n :
                res[row].append(temp90)
                res[row].append(temp180)
                res[row].append(temp270)
                
                temp90 = ''
                temp180 = ''
                temp270 = ''
                
    print(f'#{case}')        
    for row in res:
        print(' '.join(row))
        
        
        
        