
# Questão 1
print("--- Exercício 1 ---")
nome = "Marcos Sampaio"  
idade = 45             
print(f"Meu nome é {nome} e eu tenho {idade} anos.")
print("-" * 20) # Linha divisória para melhor visualização

# Questão 2
# Atribua os valores 5 e 10 às variáveis a e b. Troque os valores entre elas e imprima os resultados finais.

print("--- Exercício 2 ---")
a = 5
b = 10
print(f"Antes da troca: a = {a}, b = {b}")

# Troca de valores:
# Método 1: Usando uma variável temporária (tradicional)
# temp = a
# a = b
# b = temp

# Método 2: Troca direta (mais "pythônico")
a, b = b, a

print(f"Depois da troca: a = {a}, b = {b}")
print("-" * 20)

# Questão 3
# Crie uma constante chamada PI com valor 3.14159 e imprima o valor da área de um círculo de raio 4.

print("--- Exercício 3 ---")
# Em Python, constantes são definidas por convenção (letras maiúsculas)
PI = 3.14159
raio = 4
area = PI * (raio ** 2)
print(f"A área de um círculo com raio {raio} é: {area}")
print("-" * 20)

# Questão 4
# Crie três variáveis: uma do tipo inteiro, uma do tipo float e uma do tipo string.
# Use type() para imprimir o tipo de cada uma.

print("--- Exercício 4 ---")
var_inteiro = 100
var_float = 10.5
var_string = "Olá, Python!"

print(f"Tipo de var_inteiro: {type(var_inteiro)}")
print(f"Tipo de var_float: {type(var_float)}")
print(f"Tipo de var_string: {type(var_string)}")
print("-" * 20)

# Questão 5
# Calcule o valor da expressão 10 + 5 * 2 - 3 ** 2 e explique o resultado com base na ordem de precedência.

print("--- Exercício 5 ---")
# Expressão: 10 + 5 * 2 - 3 ** 2

# Ordem de Precedência:
# 1. Potenciação (**)
# 2. Multiplicação (*) e Divisão (/, //, %)
# 3. Adição (+) e Subtração (-)

# Passo a passo:
# 1. Potenciação: 3 ** 2 = 9
#    Expressão se torna: 10 + 5 * 2 - 9
# 2. Multiplicação: 5 * 2 = 10
#    Expressão se torna: 10 + 10 - 9
# 3. Adição/Subtração (da esquerda para a direita):
#    10 + 10 = 20
#    20 - 9 = 11

resultado_expressao = 10 + 5 * 2 - 3 ** 2
print(f"O resultado da expressão '10 + 5 * 2 - 3 ** 2' é: {resultado_expressao}")
print("Explicação: Primeiro, 3**2 (potenciação) resulta em 9. Depois, 5*2 (multiplicação) resulta em 10. Por fim, as operações de adição e subtração são realizadas da esquerda para a direita: 10 + 10 = 20, e 20 - 9 = 11.")
print("-" * 20)

# Questão 6
# Crie uma variável chamada celsius e atribua a ela um valor em graus Celsius (por exemplo, 25).
# Em seguida, converta essa temperatura para Fahrenheit usando a fórmula correspondente
# Armazene o resultado em uma variável chamada fahrenheit e exiba a seguinte mensagem com print:
# "A temperatura de [celsius]°C em Fahrenheit é [fahrenheit]°F"

print("--- Exercício 6 ---")
celsius = 25
# Fórmula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura de {celsius}°C em Fahrenheit é {fahrenheit}°F")
print("-" * 20)

# Questão 7
# Crie um programa que verifique se duas variáveis x e y são diferentes e maiores que zero.

print("--- Exercício 7 ---")
x_check = 5
y_check = 3

# Condições:
# 1. x é diferente de y (x != y)
# 2. x é maior que zero (x > 0)
# 3. y é maior que zero (y > 0)
# Usamos 'and' para garantir que todas as condições sejam verdadeiras.

sao_diferentes_e_maiores_que_zero = (x_check != y_check) and (x_check > 0) and (y_check > 0)

print(f"Para x={x_check} e y={y_check}:")
print(f"São diferentes e maiores que zero? {sao_diferentes_e_maiores_que_zero}")

# Teste com outros valores (opcional)
x_test1, y_test1 = 5, 5 # Falso (não são diferentes)
sao_diferentes_e_maiores_que_zero_test1 = (x_test1 != y_test1) and (x_test1 > 0) and (y_test1 > 0)
print(f"Para x={x_test1} e y={y_test1}: {sao_diferentes_e_maiores_que_zero_test1}")

x_test2, y_test2 = -2, 3 # Falso (x não é maior que zero)
sao_diferentes_e_maiores_que_zero_test2 = (x_test2 != y_test2) and (x_test2 > 0) and (y_test2 > 0)
print(f"Para x={x_test2} e y={y_test2}: {sao_diferentes_e_maiores_que_zero_test2}")
print("-" * 20)


# Questão 8
# Avalie a expressão (5 > 3) and (2 < 1) e explique o resultado.

print("--- Exercício 8 ---")
# Expressão: (5 > 3) and (2 < 1)

# Passo a passo:
# 1. Avaliar a primeira parte: (5 > 3)
#    5 é maior que 3? Sim. -> Resultado: True

# 2. Avaliar a segunda parte: (2 < 1)
#    2 é menor que 1? Não. -> Resultado: False

# 3. Combinar com o operador 'and': True and False
#    Para 'and', ambos os lados precisam ser True para o resultado final ser True.
#    Como um dos lados é False, o resultado final é False.

resultado_expressao_8 = (5 > 3) and (2 < 1)
print(f"O resultado da expressão '(5 > 3) and (2 < 1)' é: {resultado_expressao_8}")
print("Explicação: A primeira parte (5 > 3) é Verdadeira. A segunda parte (2 < 1) é Falsa. Como o operador 'and' exige que ambas as condições sejam Verdadeiras para que o resultado final seja Verdadeiro, e uma delas é Falsa, o resultado completo da expressão é Falso.")
print("-" * 20)

# Questão 9
# Crie uma variável chamada altura_str e atribua a ela o valor "1.75" (uma string).
# Em seguida, converta essa variável para o tipo float e armazene o resultado em uma nova variável chamada altura_float.
# Por fim, use o print para exibir a mensagem: "A altura convertida é: [altura_float]"

print("--- Exercício 9 ---")
altura_str = "1.75"
altura_float = float(altura_str) # Converte a string para float

print(f"A altura convertida é: {altura_float}")
print(f"Confirmando o tipo: {type(altura_float)}") # Opcional: para mostrar que o tipo mudou
print("-" * 20)

# Questão 10
# Crie dois conjuntos: alunos_python e alunos_java. Coloque 3 nomes em cada e:
# Mostre os alunos que fazem as duas linguagens.
# Mostre os alunos que fazem só Python.
# Mostre todos os alunos (sem repetição).

print("--- Exercício 10 ---")
# Conjuntos são definidos com chaves {} ou set().
# Para garantir que haja alunos em comum e exclusivos para demonstração, vamos usar:
alunos_python = {"Maria", "João", "Ana"}
alunos_java = {"João", "Pedro", "Carla"}

# a) Mostre os alunos que fazem as duas linguagens (interseção)
# Usamos o operador '&' ou o método .intersection()
alunos_ambas = alunos_python & alunos_java
# ou alunos_ambas = alunos_python.intersection(alunos_java)
print(f"Alunos que fazem as duas linguagens: {alunos_ambas}")

# b) Mostre os alunos que fazem só Python (diferença)
# Usamos o operador '-' ou o método .difference()
alunos_so_python = alunos_python - alunos_java
# ou alunos_so_python = alunos_python.difference(alunos_java)
print(f"Alunos que fazem só Python: {alunos_so_python}")

# c) Mostre todos os alunos (sem repetição) (união)
# Usamos o operador '|' ou o método .union()
todos_alunos = alunos_python | alunos_java
# ou todos_alunos = alunos_python.union(alunos_java)
print(f"Todos os alunos (sem repetição): {todos_alunos}")
print("-" * 20)
