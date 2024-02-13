def fib(n):
    """Print a Fibonacci series up to n"""
    a, b = 0, 1
    while a < n:
        print( a, end=' ')
        a, b = b, a+b
    print()

def fib2(n=500): # return Fibonacci series up to n
    """ Return a *list* containing the Fib Series up to n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def ask_ok(prompt, retries=4, complaint= 'Yes or No, Please'):
    while True:
        ok = input(prompt + ' ')
        print(ok)
        ok = ok.lower()
        print(ok)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no'):
            return False
        retries -= 1
        if retries < 0:
            raise OSError('Uncooperative User')
        print(complaint)