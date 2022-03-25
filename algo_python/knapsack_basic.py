# 막대기 자르기 
# 하나의 막대기가 있다. 막대기의 길이에 따라 가격이 다르다.
# 최고의 수익이 되도록 막대기를 자르라
# 이때 최고의 수익은?

# (길이,가격)
# (0,0)
# (1,1),
# (2,5),
# (3,8),
# (4,9),
# (5,10),
# (6,17),
# (7,17),
# (8,20),
# (9,24)


def solution(price,n):

# ---------------- 재귀 없이계산 -------------------------------
# 
# 각 길이에서의 최대이익 계산
# max_value = max(max_value, price[j-i] + max_values[i])
# 이전최대값인 max_value와 바로전 
# |---------------------|(j)
# |-------------|(i)            i는 (1~j) 사이에서 왔다갔다...
#               |-------| 이만큼이 아마도 (j-i) 이겠지? 그래서 가격차이는 price[j-i]이고 이건아마도 price[1]일꺼고 이건 j와i의차이만큼 달라질꺼다.
# 정상적인 각각 거리만큼의 누적값을 계산하려면, 1~i까지의 최대값인 max_values[i]를 더해준다 (이거 이해안간다 차라리 price[j]-price[i]이게 맞지않나?)
# 
    # max_values = [0]
    # max_value = 0
    # for j in range(1,n+1):
    #     for i in range(j):
    #         print(j,'.',i,'//',max_value,'/',price[j-i],'/',max_values[i])
    #         max_value = max(max_value, price[j-i] + max_values[i])
    #         # max_value = max(max_value, price[j]-price[i])
    #     max_values.append(max_value)
    # return max_values[n]


# ---------------- 재귀로 계산 -------------------------------
# 

    if n <= 0:
        return 0
    max_val = 0
    for i in range(n):
        max_val = max(max_val, price[i] + solution(price, n-i))
    return max_val


price = [0,1,5,8,9,10,17,17,20,24]
print(solution(price,8))