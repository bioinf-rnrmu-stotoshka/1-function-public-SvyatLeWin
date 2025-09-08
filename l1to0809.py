import random
def fmin (a):

    assert isinstance(a,list), "ne massiv"
    assert len(a)>0, "pustoy spisok"
    min = a[0]
    indexes=[]
    for i in range(len(a)):
        assert isinstance(a[i],(int,float,complex)) and not isinstance(a[i],bool), "ne cifry v massive"
        if a[i]<min:
            indexes.clear()
            indexes.append(i)
            min=a[i]
        elif a[i]==min:
            indexes.append(i)
    return indexes
def fibonacci (n):
    assert isinstance(n, int), 'введено не число, или не целое число'
    assert n>=0, 'введено отрицательное число'
    if n==0:
        f=0
    elif n==1:
        f=1
    else:
        f=fibonacci(n-1)+fibonacci(n-2)
    return f
print(fibonacci(6))
def isc(n,a):
    s=0
    assert isinstance(n, int), 'ошибка с числом элементов массива'
    assert isinstance(a, list), 'не введен массив'
    for i in a:
        assert isinstance(i, int), 'в массиве присутствуют не целые числа'
    for i in range(1,n):
        k=a[i]
        j=i-1
        while j>=0 and a[j]>k:
            a[j+1]=a[j]
            s+=1
            j-=1
        a[j+1]=k
    return s
print(isc(6,[6,10,4,5,1,2]))
def counuc(s):
    count=[0,0,0,0]
    assert isinstance(s, str), 'введена не строка'
    assert set(s).issubset({'A','C','G','T'}), 'Присвутствуют посторонние символы'
    for i in s:

        if i=='A':
            count[0]+=1
        elif i=='C':
            count[1]+=1
        elif i=='G':
            count[2]+=1
        elif i == 'T':
            count[3] += 1

    return count
print(*counuc('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))
def trdnatrna(s):
    assert isinstance(s, str), 'введена не строка'
    assert set(s).issubset({'A', 'C', 'G', 'T'}), 'Присвутствуют посторонние символы'
    r=s.replace("T","U")
    return r
print(trdnatrna("GATGGAACTTGACTACGTAAATT"))
def comdna(s):
    assert isinstance(s, str), 'введена не строка'
    assert set(s).issubset({'A', 'C', 'G', 'T'}), 'Присвутствуют посторонние символы'
    c={'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    cs=''.join(c[i] for i in s)
    return cs[::-1]
print(comdna("AAAACCCGGT"))
def rrr(n, k, memo=None):
    assert isinstance(n, int) and isinstance(k, int), 'введены не числа'
    assert n > 0 and k > 0, 'введены отрицательные числа'
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        memo[n] = 1
    if n == 1 or n == 2:
        return 1
    return rrr(n - 1, k, memo) + k * rrr(n - 2, k, memo)
print(rrr(5, 3))
def degray(n,m,edges):
    assert isinstance(n, int), 'n и m должны быть числами'
    assert isinstance(m, int), 'n и m должны быть числами'
    assert 1 <= n <= 1000, "n должно быть между 1 и 1000"
    assert m >= 0, "m должно быть >=0"
    assert isinstance(edges, list), 'edges должен быть массивом'
    assert len(edges) == m, "Число ребер не совпадает с m"
    degrees = [0] * n
    for u, v in edges:
        assert 1 <= u <= n and 1 <= v <= n, "Неправильно указаны номера вершин"
        assert u != v, "Ребро должно размещаться между двумя разными вершинами"
        degrees[u - 1] += 1
        degrees[v - 1] += 1
    return degrees
print(*degray(6,7,[(1,2),(2,3),(6,3),(5,6),(2,5),(2,4),(4,1)]))