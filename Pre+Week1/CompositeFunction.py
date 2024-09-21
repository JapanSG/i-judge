"""CompositeFunction"""
def f(x):
    """Function"""
    return 2*x
def g(x):
    """Function"""
    return x/2 + 1

a = int(input())
print(f"{f(g(a)):.2f}")
print(f"{g(f(a)):.2f}")
