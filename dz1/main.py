def polindrom(val):
    result = True
    reverse_val = val[::-1]
    for index in range(len(val)):
        symbol1 = val[index]
        symbol2 = reverse_val[index]
        if symbol1 != symbol2:
            result = False
            break
    return result

a = input('введите строку ')
print(polindrom(a))