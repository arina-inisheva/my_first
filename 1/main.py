def strcounter(string):
    for synbol in set(string):
        counter = 0
        for sub_symbol in string:
            if synbol == sub_symbol:
                counter += 1
        print(synbol, counter)

strcounter('abeeaccde')

#def strcounter(string):
#  for symbol in string:
#   counter = 0
#  for sub_symbol in string:
#       if symbol == sub_symbol:
#       counter += 1
# print(symbol, counter)

# strcounter('aaabbcdeee')

def strcounter(string): # сложность O(n)
    syms_counter = {}
    for symbol in string:
        syms_counter[symbol] = syms_counter.get(symbol, 0) + 1
print(syms_counter)

strcounter('aaabbcdeee')