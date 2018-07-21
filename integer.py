from typing import List, Union

x="5"
y="10"
#print(type(x+y))
#print(x+y)

x=5
y=10
#print(type(x*y))
#print(x*y)

x=5
y=10
z=x/y

#print(z)
#print(type(z))

###################type change

#print(str(z))

###################bool

dogru = True
Yanlis = False

#print(dogru == False)


liste =[ x, y, "elma",dogru,z,"yeni"]

liste.append("armut")
liste.insert(0,"yeni")
#print(liste)

cikarilan=liste.remove(liste[4])
#print(cikarilan)

liste2=[5,4,3,2,1]

liste.append(liste2)
#print(liste)
#print(liste2)
#print(liste[liste.index(liste2)])

liste.extend(liste2)
#print(liste)


liste3=sorted(liste2)
#print(liste2)
#print(liste3)

liste4=[2,6,1,9,10,2,1]
liste4.sort(reverse=True)
#print(liste4)

#print(liste4.count(1))
#print(len(liste4))
print(max(liste4))
print(min(liste4))