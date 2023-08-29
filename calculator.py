from itertools import product
import numpy as np
hedef = int(input("toplam hedefini giriniz"))
liste = [int(x) for x in str(input("Listeyi 'a,b,c' formatında virgül ile ayırarak giriniz ")).split(",")]
def find_product(liste,hedef,show):
    answs = []
    for uzunluk in range(1,len(liste)+1):
        perm = list(product(liste,repeat=uzunluk))
        for numbers in perm:
            summ = 0
            for num in numbers:
                summ+=num
            if summ == hedef:
                answs.append(numbers)
    lengts = [len(x) for x in answs]
    #print(lengts)

    lastansws = zip(lengts,answs)
    sortedansws = sorted(lastansws,key= lambda x: x[1])
    sortedansws.reverse()
    if show:
        return sortedansws
    else:
        return sortedansws[0][1]
print(find_product(liste,hedef,show=1))
#tüm kombinasyonları görmek için show=1



