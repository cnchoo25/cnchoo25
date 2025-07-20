def snail(x,y,d,n):
    
    array = [[0]*n for _ in range(n)]
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    for num in range(1,n**2+1):
        
        array[x][y] = num
        temp_x = x + dx[d]
        temp_y = y + dy[d]
        
        if (0 <= temp_x < n) and (0 <= temp_y < n) and array[temp_x][temp_y] == 0:
            x, y = temp_x, temp_y
        else:   
            d = (d+1) % 4
            x += dx[d]
            y += dy[d]
                  
    return array

t = int(input())

for num in range(1,t+1):
    
    n = int(input())
    res = snail(0,0,0,n)
    
    print(f'#{n}')
    for row in range(n):
        print(*res[row])
    
    