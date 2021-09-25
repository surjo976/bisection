def f(x):
    return 4*(x*x*x)-6*(x*x)+7*x-2.3

def bisection(a,b,e):
    x0=1
    xr=0
    dx=b-a
    print("-----------Bisection Methhod ------------")
    condition = True
    while condition:
        xr=(a+b)/2
        print("===================================")
        print ('Iteration no : %d \nRoot obtained = %0.6f \nEstimate Error = %0.6f' % (x0,xr,f(xr)))
        if(f(a)*f(xr)<0):
            b=xr
            dx=b-a
        else:
            a=xr
            dx=b-a
        x0=x0+1
        condition=abs(f(dx))>e  and f(xr)!=0
    print("=====================================")
    print("-------------------------------------")
    print("=============Finally=================")
    print ('Iteration no : %d \nRoot obtained = %0.6f \nEstimate Error = %0.6f' % (x0-1,xr,f(xr)))

#input Section
a=float(input("Enter First Guess: "))
b=float(input("Enter Second Guess: "))
e=float(input("Enter Tolerable error: "))

if f(a)*f(b)>0:
    print ("***********You Enter wrong Guess Value*********** \n Try Again")
else:
    bisection(a,b,e)
