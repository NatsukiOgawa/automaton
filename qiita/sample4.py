N=int(input('scale=')) #横の長さ
K=int(input('length=')) #縦の長さ

import random
init=input('initial state?[random/point]')
if init=='random':
    X=[random.choice([0,1]) for i in range(2*N+1)]
else:
    X=[0]*N+[1]+[0]*N
rule=int(input('rule=')) #0〜255
rule=('0'*8+bin(rule)[2:])[-8:] #ruleを2進数で表す

for i in range(K):
    print(''.join([[' ','*'][i] for i in X]))
    X=[int(rule[7-(([0]+X+[0])[i-1]*4+([0]+X+[0])[i]*2+([0]+X+[0])[i+1]*1)]) for i in range(1,len(X)+1)]
