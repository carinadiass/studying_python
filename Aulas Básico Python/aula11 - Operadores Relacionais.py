"""
Operadores Relacionais
== Igualdade
> Maior que
>= Maior ou igual a
< Menor que
<= Menor ou igual a
!= Diferente
"""

print( 2 == '2')

"""Se pode pegar empréstimo se idade maior de 18"""

nome = input("Qual seu nome?\n")
idade = int(input("Qual sua idade?\n"))

#Limie te para pegar empréstimo
idade_min = 18 # Muito Jovem
idade_max = 30 # Passou da idade

if idade >= idade_min and idade<=idade_max:
    print(f"Pode {nome} solicitar empréstimo")
else:
    print(f"Não {nome} pode pegar empréstimo")