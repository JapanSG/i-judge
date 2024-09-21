'''niwarn_world'''
import math
def x_function(n : float) -> float:
    '''return x(n)'''
    return 2+math.log2(n**2)/(2*n*math.log2(n))
def y_function(n : float, s : float) -> float:
    '''return y(n,s)'''
    return (math.sin(math.radians(30))+math.sqrt(2*s))/(x_function(n)+3)
def z_function(k : float) -> float:
    '''return z(k)'''
    return (y_function(k,k)**2)+(8456*(x_function(k)**4))/(24*k)
def main():
    '''Driver Code'''
    n = float(input())
    s = float(input())
    k = float(input())
    x = x_function(n)
    y = y_function(n,s)
    z = z_function(k)
    print(f"X: {x:.1f}, Y: {y:.1f}, Z: {z:.1f}")
main()
