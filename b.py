import numpy
def bisect(f, a, b,ite,y_ant, tol=1e-8):
    fa = f(a,y_ant,ite)
    fb = f(b,y_ant,ite)
    i = 0
    # Just checking if the sign is not negative => not root  necessarily
    if numpy.sign(fa*fb) >= 0:
        print('f(a)f(b)<0 not satisfied!')
        return None

    #Printing the evolution of the computation of the root
    print(' i |     a     |     c     |     b     |     fa    |     fc     |     fb     |   b-a')
    print('----------------------------------------------------------------------------------------')

    while(b-a)/2 > tol:
        c = (a+b)/2.
        fc = f(c,y_ant,ite)
        print('%2d | %.7f | %.7f | %.7f | %.7f | %.7f | %.7f | %.7f' %
              (i+1, a, c, b, fa, fc, fb, b-a))
        # Did we find the root?
        if fc == 0:
            print('f(c)==0')
            break
        elif numpy.sign(fa*fc) < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        i += 1

    xc = (a+b)/2.
    return xc
M = 10
equis = lambda i : 100*i/M
func = lambda ym1, y, i: ((equis(i+1)-equis(i))/2)*((ym1*numpy.cos(equis(i+1)+ym1))+(y*numpy.cos(equis(i)+y)))+y-ym1
res_inicio = 1
res_fin = 1
y_ant = 1
tol = 1e-8
total_intentos = 0

for i in range(0,M+1):
    x_inicio = -numpy.pi
    x_fin = numpy.pi
    res_inicio = func(x_inicio,y_ant,i)
    res_fin = func(x_fin,y_ant,i)
    intentos = 1
    print("["+str(res_inicio)+", "+str(res_fin)+"]")
    while numpy.sign(res_inicio) == numpy.sign(res_fin):
        x_inicio -= 1
        x_fin += 1
        res_inicio = func(x_inicio,y_ant,i)
        res_fin = func(x_fin,y_ant,i)
        intentos += 1

        total_intentos+= intentos
    print("El intervalo es el siguiente" +str(x_inicio)+" "+str(x_fin)+ "+ , obtenido en {intentos} iteraciones")
    y_ant = bisect(func,x_inicio,x_fin,i,y_ant)
