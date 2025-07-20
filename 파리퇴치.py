# t = int(input())

# for case in range(1,t+1):
#     n, m = map(int,input().split())
    
#     array = []
#     for _ in range(n): # input 행렬
#         a = list(map(int,input().split()))
#         array.append(a)

# row_sum = sum(array[m])
# col_sum = sum([col[m] for col in array])
# res = row_sum + col_sum - array[m][m]

n, m = 6,3

array = [
    [29, 21, 26, 9, 5, 8],
    [21, 19, 8, 0, 21, 19],
    [9, 24, 2, 11, 4, 24],
    [19, 29, 1, 0, 21, 19],
    [10, 29, 6, 18, 4, 3],
    [29, 11, 15, 3, 3, 29]
]


res_cand = []
for i in range(m-1,n-m+1):
    for j in range(m-1,n-m+1):

            # cross
            row_sum = sum(array[i][y] for y in range(j-(m-1), j+(m-1)+1))
            col_sum = sum(array[x][j] for x in range(i-(m-1), i+(m-1)+1))
            res1 = row_sum + col_sum - array[i][j]
            res_cand.append(res1)
            
            # diagoanl
            uy,ly,lx,rx = 0,0,0,0
            upper_sum, lower_sum = 0,0
            for _ in range(m-1):
                uy -= 1
                ly += 1
                lx -= 1
                rx += 1
                upper_sum += array[i+lx][j+uy] + array[i+rx][j+uy]
                lower_sum += array[j+lx][j+ly] + array[j+rx][j+ly]
                res2 = upper_sum + lower_sum + array[i][j]
            res_cand.append(res2)
                
            print(res_cand)
              
# print(f'#{case} {max(res_cand)}')       
            
            



