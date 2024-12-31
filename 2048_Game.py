import random as rand
def start():
    m=[]
    for i in range(4):
        m.append([0]*4)
    print('Controles :')
    print('"W" or "w" for moving up')
    print('"A" or "a" for moving left')
    print('"S" or "s" for moving down')
    print('"D" or "d" for moving right')

    set_2(m)
    return m

def set_2(m):
    r=rand.randint(0,3)
    c=rand.randint(0,3)
    while m[r][c]!=0:
        r=rand.randint(0,3)
        c=rand.randint(0,3)

    m[r][c]=2
    return m


def status(m):
    for i in range(4):
        for j in range(4):
            if m[i][j]==2048:
                return 'WON'
    
    for i in range(4):
        for j in range(4):
            if m[i][j]==0:
                return'Continue'

    for i in range(3):
        for j in range(3):
            if m[i][j]==m[i][j+1] or m[i][j]==m[i+1][j] :
                return'Continue'
    
    for i in range(3):
        if m[i][3] == m[i+1][3]:
            return 'Continue'
    for j in range (3):
        if m[3][j]==m[3][j+1]:
            return 'Continue'
    
    return 'Lost'

def shift(m):
    change = False
    nm=[]
    for i in range(4):
        nm.append([0]*4)
    for i in range(4):
        pos=0
        for j in range(4):
            if m[i][j]!=0:
                nm[i][pos]=m[i][j]
                if j!=pos:
                    change=True
                pos+=1
    return nm,change

def merge(m):
    change = False
    for i in range(4):
        for j in range(3):
            if m[i][j]==m[i][j+1] and m[i][j]!=0:
                m[i][j]=m[i][j]*2
                m[i][j+1]=0
                change=True
    return m,change

def drop(m):
    nm=[]
    for i in range(4):
        nm.append([])
        for j in range(4):
            nm[i].append(m[j][i])
    return nm

def reverse(m):
    nm=[]
    for i in range(4):
        nm.append([])
        for j in range(4):
            nm[i].append(m[i][3-j])
    return nm

def left(g):
    ng,change1=shift(g)
    ng,change2=merge(ng)
    changed=change1 or change2
    ng,temp=shift(ng)
    return ng,changed

def right(g):
    ng=reverse(g)
    ng,changed=left(ng)
    ng=reverse(ng)
    return ng,changed

def up(g):
    ng=drop(g)
    ng,changed=left(ng)
    ng=drop(ng)
    return ng,changed

def down(g):
    ng=drop(g)
    ng,changed=right(ng)
    ng=drop(ng)
    return ng,changed

m=start()
for i in range(4):
    print(m[i])
while True:
    x=input('Enter your command:')
    if x=='w' or x=='W':
        m,cha=up(m)
        stats=status(m)
        print(stats)
        if stats=='Continue':
            set_2(m)
        else:
            break
    elif x=='a' or x=='A':
        m,cha=left(m)
        stats=status(m)
        print(stats)
        if stats=='Continue':
            set_2(m)
        else:
            break
    elif x=='s' or x=='S':
        m,cha=down(m)
        stats=status(m)
        print(stats)
        if stats=='Continue':
            set_2(m)
        else:
            break
    elif x=='d' or x=='D':
        m,cha=right(m)
        stats=status(m)
        print(stats)
        if stats=='Continue':
            set_2(m)
        else:
            break
    else:
        print('Invalid command')
    for i in range(4):
        print(m[i])