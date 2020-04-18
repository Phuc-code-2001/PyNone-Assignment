def change_base(num, base = 2):
    result = ''
    while num != 0:
        q = num % base
        result = str(q) + result 
        num = num // base
    return result

a = change_base(215)
print(a)