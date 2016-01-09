def gen_secv(n):
    perm = [1,for i in range(0,n)]
    while perm[0] < n +1:
        perm[n-1] +=1
        poz = n-1
        while perm[poz] == n:
            perm[poz]  -=n
            perm[poz-1]+=1
            poz-=1
