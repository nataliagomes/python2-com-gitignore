#import random

#lista=[]
#i=1 ( para chamar o python no terminal , exist() depois coloca py e o nome do seu arquino )
    
#for i in range(15):
 #   n= None
  #   while (n in lista):
   #     n=random.randint(1,15)
   #     lista.append(n)
  
import random as r
import statistics
   
v_lista=[]
i=1
    
while i <= 20:
    v_lista.append(r.randrange (1, 100, 3))
    i = i+1
print (f'Essa foi a lista gerada aleatoriamente: {v_lista}')

def maior_valor(v_lista):
    return max(v_lista, key=int)

print (f'Retorne o maior numero da lista: {maior_valor(v_lista)}')

def media_lista(v_lista):
    return statistics.mean(v_lista)

print (f'Retorne a media da lista : {media_lista(v_lista)}')

