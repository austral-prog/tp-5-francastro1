def roots(a, b, c):
    import math
    discriminant=((b**2)-4*a*c)
    if discriminant>0:
        x1=float((-b+math.sqrt(discriminant))/(2*a))
        x2=float((-b-math.sqrt(discriminant))/(2*a))
        return f"({x1}, {x2})"
    elif discriminant==0: 
        x1=float((-b/(2*a)))
        return f"({x1})"
    else:
        return "( )"
cuadratica=roots(1,-3,2)
print(cuadratica)

def value_y(a, b, c, x):
    y=a*x**2+b*x+c
    return y 
funciony=value_y(1,-3,2,0)
print(funciony)

def to_string(a, b, c):
    if a!=0 and b!=0 and c!=0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a==0 and b!=0 and c!=0:
        return f"f(x) = {b} * X + {c}"
    elif a!=0 and b==0 and c!=0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a!=0 and b!=0 and c==0:
        return f"f(x) = {a} * X^2 + {b} * X"
    elif a==0 and b==0 and c!=0:
        return f"f(x) = {c}"
    elif a!=0 and b==0 and c==0:
        return f"f(x) = {a} * X^2 "
    elif a==0 and b!=0 and c==0:
        return f"f(x) = {b} * X"
quadfn=to_string(2, -3, 1)
print(quadfn)

def derivation(a, b, c):
    if a!=0 and b!=0:
        a=2*a
        b=b
        return f"f'(x) = {a} * X + {b}"
    elif a!=0 and b==0:
        a=2*a 
        return f"f'(x) = {a} * X" 
    elif a==0 and b!=0:
        a=2*a 
        b=b
        return f"f'(x) = {b}" 
    elif a==0 and b==0:
        return f"f'(x) = 0"
derivada=derivation(2,-3,1)
print(derivada)
