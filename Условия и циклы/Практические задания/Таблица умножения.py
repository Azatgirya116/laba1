for x in range(2,10) :
    for y in range(2, 10) :

     if y != 9 :
         print(f'{x * y:2}', end=' ')
     else :
         print(x * y, end='')
         print()