def exponent(x:float) ->float: 
    e = float(0)
    j = float(1)
    x2 = x
    x1 = float(x2)
    for i in range(200):
        if i == 0 :
            e = +1
        else:
            e = e + x1/j
            i1 = i+1
            j = j*(i1)
            x1 = x*x1
    return e

def abs_val(x):
    if x>=0:
        return x
    else:
        return -x
def Ln(x:float)-> float:
    epsilon = 0.001
    y_prev = x-1.0
    y_curr = 0.0
    if x <= 1:
        return 0
    while abs_val(y_curr-y_prev) > epsilon:
        y_prev = y_curr
        y_curr = y_prev + 2*(x-exponent(y_prev))/(x+exponent(y_prev))
    return y_curr

def XtimesY(x:float , y:float)->float:
    if x<=0:
        return 0
    return float('%0.6f' % exponent(y*Ln(x)))

def sqrt(x:float,y:float) -> float:
    if x ==	0 or y<0:
        return 0
    return XtimesY(y, 1/x)

def calculate(x:float) -> float:
    return exponent(x)*XtimesY(7, x)*XtimesY(x, -1)*sqrt(x,x)
