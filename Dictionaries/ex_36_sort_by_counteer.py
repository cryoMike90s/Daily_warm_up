from collections import Counter

dict_1 = {'Math':81, 'Physics':83, 'Chemistry':87}

z = Counter(dict_1)
c = z.most_common()
print(c)
print(type(c[1]))