def pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    hasil = 1
    
    for i in range(0, n):
        hasil *= x
    return(hasil)
    return 0

if __name__ == '__main__':
    print(pow(2, 3)) # 8
    print(pow(7, 2)) # 49
    print(pow(10, 5)) # 100000
    print(pow(17, 6)) # 24137569
    print(pow(5, 3)) # 125