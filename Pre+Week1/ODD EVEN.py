"""ODDEVEN"""
def is_odd(num):
    """Return True if odd. Else return False"""
    if not num%2:
        return False
    return True

print(is_odd(int(input())))
