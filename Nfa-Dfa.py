import queue
f = open("date.in")
n = int(f.readline())
alfabet = [i for i in f.readline().split()]
q0 = int(f.readline())
stari_finale = {int(x) for x in f.readline().split()}
automat=[{} for i in range(n)]
for i in range(n):
    for j in alfabet:
        automat[i][j]=set()
st = f.readline()
while st!="":
    (st1,car,st2)=[i for i in st.split()]
    if car not in automat[int(st1)]:
        automat[int(st1)][car]=set()
    automat[int(st1)][car].add(int(st2))
    st=f.readline()
print("NFA-ul este:",automat)
#Eliminarea Nedeterminismului

coada=queue.Queue()
aux = set()
for i in alfabet:
    aux = aux.union(automat[q0][i])

coada.put(tuple(aux))
vizita = [tuple([q0]),tuple(aux)]

while not coada.empty():
    a = coada.get()
    for i in alfabet:
        aux = set()
        for j in a:
            aux=aux.union(automat[j][i])

        aux = tuple(aux)
        if aux not in vizita:
            coada.put(aux)
            vizita.append(aux)


#Calcularea starilor finale

stare_finala=[]
for i in range(len(vizita)):
    for j in vizita[i]:
        if j in stari_finale:
            stare_finala.append(i)

print("Starea finala este:" , stare_finala)


dfa = [{} for i in range(len(vizita))]

#Redenumirea starilor

for i in range(len(vizita)):
    for j in alfabet:
        aux = set()
        for k in vizita[i]:
            aux = aux.union(automat[k][j])
        if aux!=set():
            dfa[i][j]=vizita.index(tuple(aux))

print("DFA-ul creat este:",dfa)
