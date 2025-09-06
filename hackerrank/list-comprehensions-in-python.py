x = int(input())
y = int(input())
z = int(input())
n = int(input())
x_list = []
y_list = []
z_list = []
f_list = []

if x+y+z==0:
    print(f_list)
    exit()

def xf():
    for i in range(0,x+1):
        x_list.append(i)

def yf():
    for j in range(0,y+1):
        y_list.append(j)

def zf():
    for k in range(0,z+1):
        z_list.append(k)

xf()
yf()
zf()

p = [[a,b,c] for a in x_list for b in y_list for c in z_list]
q = len(p)-1

while q>=-1:
    if sum(p[q]) == n:
        p.pop(q)
    else:
        q -= 1

print(p)
