def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x>y:
        return x 
    elif y>x: 
        return y
max_of_two(2,-1)

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if x>y and x>z:
        return x 
    elif y>x and y>z:
        return y 
    elif z>x and z>x: 
        return z
max_of_three(3,7,-8)
