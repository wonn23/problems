def similar_fibonach(n):
    if n<=3:
        return 1
    else:
        sfibo = [0] * n
        sfibo[0] = 1
        sfibo[1] = 1
        sfibo[2] = 1

        for i in range(3,n):
            sfibo[i] = sfibo[i-3] + sfibo[i-1]
        return sfibo[n-1]
print(similar_fibonach(int(input())))