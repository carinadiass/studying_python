"""
Tipos de dados:

str - string - textos - 'assim' ou "assim"
int - inteiro - 111 - 1 - 0 -4 4
float - real / ponto flutuante 1.3 - -0.3
bool - booleano/lógico - True ou False / 10==10 - Valor lógico (Verdadeiro ou Falso)

"""
print(type('Carina'))  # <class 'str'> Type retorna o tipo de valor  neste caso foi um string
print(type(True))  # <class 'bool'>
print(type(12))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print('11'==11, type('11'==11))  # <class 'bool'>

# Convertendo um tipo para outro
print('Carina',type('Carina'),bool('Carina'))
print('10',type('10'),type(int('10')))

# print(int('20.4')) # <class 'str'> ValueError: invalid literal for int() with base 10: '20.4'

#Exercicio

#String: Nome
print('Carina',type('Carina'))

#Idade: Int
print(33,type(33))

#Altura: Float

print(1.69,type(1.69))


# É maior de 18 anos 10>20
print(33>20,type(33>20))
