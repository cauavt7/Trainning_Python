print("esse é o sistema de simuladorde tabuada\n")

numero = int(input("Digite quanto o numero que quer resolver"))
vezes = int(input("digite por quanto voce que multiplicar"))
for n in range (1,11):
    total =  n * (numero *vezes)
    print(f" {numero} * {vezes} = {total}")
    break
    
 
 