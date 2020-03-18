f = open("date.in")
n = int(f.readline())
alfabet = [x for x in f.readline().split()]
q0 = int(f.readline())
stare_finala = {int(x) for x in f.readline().split()}
l=[{} for i in range(n)]
tranzitie = f.readline()
while tranzitie!="":
    (st1,car,st2)=[x for x in tranzitie.split()]
    if car not in l[int(st1)]:
        l[int(st1)][car]=set()
    l[int(st1)][car].add(int(st2))
    tranzitie = f.readline()

def evalueaza(cuv,stare):
    stare_curenta = stare
    stare_veche = set()
    while stare_veche!=stare_curenta:
        stare_veche=stare_curenta
        for x in stare_veche:
            if '$' in l[x]:
                stare_curenta = stare_curenta.union(l[x]['$'])

    if cuv=="":
        return stare_finala.intersection(stare_curenta)!=set()
    else:
        aux = set()
        for x in stare_curenta:
            if cuv[0] in l[x]:
                aux=aux.union(l[x][cuv[0]])

        return evalueaza(cuv[1:],aux)
a = set()
a.add(q0)
print('abxyyyxyby -',evalueaza('abxyyyxyby',a))
print('bcax - ',evalueaza('bcax',a))
print('bvbxxy - ',evalueaza('bvbxxy',a))
print('abyyxz - ',evalueaza('abyyxz',a))
print('abyyxyx - ',evalueaza('abyyxyx',a))