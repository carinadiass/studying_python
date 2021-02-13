"""
+  (Adição)
-  (Subtração)
*  (Multiplicação)
/  (Divisão)
// (Divisão Inteira)
** (Potenciação)
%  (Módulo)
() (Operador de precedencia)

"""

print( 'Adição',10+10)
print('Subtração',10-10)

#Detalhes de multipicação

# print('Multiplicação','10' * '10')  # TypeError: can't multiply sequence by non-int of type 'str'

print('Multiplicação *','10' * 10)  # Multiplicação 10101010101010101010 (Operador de Repetição)

print('Adição +', '10' + 'OI')  # Adição + 10OI (Operador de concatenação)

print(10.3//3)  # Resultado: 3.0 (Divisão Inteira)

print(10.3/3)  # Resultado: 3.4333333333333336 (Divisão Normal)

print(5+2*10)  # Resultado: 25

print((5+2)*10)  #Resultado: 70  (Utlização do parentese para alterar a precedencia)
