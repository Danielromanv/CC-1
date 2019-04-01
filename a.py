import numpy
def bisect(f, a, b,ite,y_ant, tol=1e-8):
    fa = f(a,y_ant,ite)
    fb = f(b,y_ant,ite)
    i = 0
    # Just checking if the sign is not negative => not root  necessarily
    if np.sign(fa*fb) >= 0:
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
        elif np.sign(fa*fc) < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        i += 1

    xc = (a+b)/2.
    return xc


M=10
equis = lambda i : 100*i/M
func = lambda i, ym1, y: ((equis(i+1)-equis(i))/2)*(ym1*numpy.cos(equis(i+1)+ym1)+y*numpy.cos(equis(i)+y))+y-ym1
f_inicio = 1
f_fin=1
efe = 1
for i in range(0,M+1):
    print("i = ",i)
    y_inicio = -1
    y_fin =1
    f_inicio = func(i,y_inicio,f_inicio)
    print("y = ",y_inicio," y+1= ", f_inicio )
    print("f = ",f_inicio)
    f_fin = func(i,y_fin,f_fin)
    print("f = ",f_fin )
    print(f"[{f_inicio},{f_fin}]")
    while numpy.sign(f_inicio)==numpy.sign(f_fin):
        y_inicio*=2
        y_fin*=2
        f_inicio = func(i,y_inicio,efe)
        f_fin = func(i,y_fin,efe)
