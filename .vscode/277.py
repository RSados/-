import keyword

str = ['print','boolean','True','int']
for i in range(len(str)):
    print(keyword.iskeyword(str[i]))

print(keyword.kwlist)