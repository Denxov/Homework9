def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, result - 1):
            if result % i == 0:
                print('Составное')
                return result
        print('Простое')
        return result

    return wrapper


@is_prime
def sum_three(n1, n2, n3):
    return n1 + n2 + n3


result = sum_three(2, 3, 6)
print(result)
