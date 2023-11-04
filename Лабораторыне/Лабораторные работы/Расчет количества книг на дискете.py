# TODO Найдите количество книг, которое можно разместить на дискете
ves=1.44
colv=100
str=50
sym=25
razmer=1024*1024
cod=4

obem=colv*str*sym*cod/razmer
kolichestvo=ves//obem
print("Количество книг, помещающихся на дискету:", round(kolichestvo))
