def Lista1(lista, num):
    for item in lista:
        if item > num:   #Filtro   
            print(item)

num = 5 
lista = [0,1,2,3,4,5,6,7,8,9]
Lista1(lista, num)