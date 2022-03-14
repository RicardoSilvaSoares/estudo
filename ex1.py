#faça 1 programa que leia nomes e pesos guardando em ma lista e mostre no final:
#A)quantas pessoas foram cadastradas
#B)listagem das mais pesadas
#3)Listagem das mais leves 

from multiprocessing.sharedctypes import Value


temp = [] #lista temporatia
princ = [] #lista principal
maior_p = menor_p = 0 
levs =[]
#criei um laço infinito com uma condição de para para coletar os dados
while True:
    temp.append(str(input("nome: ")))
    temp.append(float(input("peso: ")))
    if len(temp) == 0 :
        maior_p = menor_p = temp[1]
    else:
        if temp[1] > maior_p:
            maior_p = temp[1]
        if temp[1] < menor_p:
            menor_p = temp[1]
    
    princ.append(temp[:])
    temp.clear()

    condi= str(input("Deseja finalizar? [S/N]"))
    if condi in "Ss":
        break

print("-="*30)
print(f"O dados foram {princ}")    
print(f"O numero de pessoas cadastradas foi: {len(princ)}")
print(f"O maior peso foi {maior_p} kg. Peso de " ,end ="")
for p in princ:
    if p[1] == maior_p:
        print(f"[{p[0]}]" , end ="")
    
print()
print(f"Omenor peso foi {menor_p} kg. Peso de", end ="")
for p in princ:
    if p[1] == menor_p:
        print(f"[{p[0]}]", end="")
    
print()