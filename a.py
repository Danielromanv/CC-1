import numpy

M=40
equis = lambda i, M : 100*i/M
func = lambda i, M, ym1, y: ((equis(i+1,M)-equis(i,M))/2)*(ym1*numpy.cos(equis(i+1,M)+ym1)+y*numpy.cos(equis(i,M)+y))+y-ym1
f_inicio = 1
f_fin=1
l = dict()
for i in range(0,M+1):
    print("i = ",i)
    y_inicio = -1000
    y_fin =1000
    f_inicio = func(i,M,y_inicio,f_inicio)
    print("y = ",y_inicio," y+1= ", f_inicio )
    print("f = ",f_inicio)
    f_fin = func(i,M,y_fin,f_fin)
    if numpy.sign(f_inicio)!=numpy.sign(f_fin):
        print("min ", abs(f_inicio-f_fin))
        l[i]= abs(f_inicio-f_fin)
        print("f = ",f_fin )
        print(f"[{f_inicio},{f_fin}]")

print(l)
print(min(l, key=l.get),l[min(l, key=l.get)])
