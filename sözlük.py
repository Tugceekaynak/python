sozluk = {'one' : '1','two':[2,10,3,1]}

#print(sozluk.get('two'))

sozluk['one']=1
#print(sozluk)

sozluk.update({'two':2})
#print(sozluk)

sozluk.update({1:'one'})
sozluk['four']=4
#print(sozluk)

del sozluk['one']

#print(sozluk)

sozluk.pop('two')
#print(sozluk)

print(sozluk.items())
print(sozluk)
print(sozluk.keys())
print(sozluk.values())