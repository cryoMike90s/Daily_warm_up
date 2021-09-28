"""Write a Python script to concatenate following dictionaries to create a new one."""

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

#First solution - python > 3.5
dic4 = {**dic1, **dic2, **dic3}
print(dic4)

#Second solution - python > 3.9

dic5 = dic1 | dic2 | dic3
print(dic5)

#Third solution - most wide spread around the globe

dic6 ={}

for d in (dic1, dic2, dic3):
    dic6.update(d)

print(dic6)