# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais
numero1=int(input('Digite o 1º número:'))
numero2=int(input("Digite o 2º número: "))
maior = numero1
print (f"os números que você adicionou foi {numero1} e {numero2}")
if numero1 < numero2:
    maior = numero2
    print(f"O número {numero2} é o maior número e o {numero1} é o menor número.")
elif numero1 == numero2:
    print("Não existe valor maior, os dois são iguais")
else:
    print(f"O número{numero1} é o maior número e o {numero2} é o menor número.")