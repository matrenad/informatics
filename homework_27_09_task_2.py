n = int(input("Введите натуральное число, не равное 1" + '\n'))
def prime_factors(n):
    if ('int' in str(type(n))) and (n>1):
        for i in range (2, n):
            if n % i == 0:
                return [i] + prime_factors(n//i)
        return [n]
    else:
        print ('Ошибка! Число должно быть натуральным и не должно равняться 1')
print(prime_factors(n))
        
