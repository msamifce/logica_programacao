# Exercício (Tarefa 2)
# Questão 1
print("===> Questão 1")
nome = "Marcos Sampaio"  
idade = 45             
print(f"Meu nome é {nome} e eu tenho {idade} anos. ")
print("=" * 45) # Linha divisória 

# Questão 2
print("\n===> Questão 2")
a = 5
b = 10
print(f"Valor original: a = {a}, b = {b}")
a_orig = a 
b_orig = b

# Segundo pesquisas, poderia ser por variável temporária
# temp = a
# a = b
# b = temp
# Mas foi feito de forma mais moderna:
a, b = b, a   # Método 2: Troca direta (mais "pythônico")

print(f"Depois da troca: a = {a}, b = {b}")
print("=" * 30)

# Questão 3

print("\n===> Questão 3")
PI = 3.14159
raio = 4
area = PI * (raio ** 2)
print(f"A área de um círculo com raio {raio} é: {area}")
print("=" * 45)

# Questão 4
print("\n===> Questão 4")
var_inteiro = 100
var_float = 10.5
var_string = "Hello world"

print(f"Tipo de var_inteiro: {type(var_inteiro)}")
print(f"Tipo de var_float: {type(var_float)}")
print(f"Tipo de var_string: {type(var_string)}")
print("=" * 35)

# Questão 5
print("\n===> Questão 5")
resultado_expressao = 10 + 5 * 2 - 3 ** 2
print(f"O resultado da expressão '10 + 5 * 2 - 3 ** 2' é: {resultado_expressao}")
print("Explicação: O resultado se deu pq primeiro, 3**2 (potenciação) resulta em 9.")
print("Depois, 5*2 (multiplicação) resulta em 10. ")
print("Por fim, as operações de adição e subtração são realizadas da esquerda para a direita: 10 + 10 = 20, e 20 - 9 = 11.")
print("=" * 120)

# Questão 6
print("\n\n===> Questão 6")
celsius = 25
# Fórmula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura de {celsius}°C em Fahrenheit é {fahrenheit}°F")
print("=" * 45)

# Questão 7
print("\n\n===> Questão 7")
x_check = 5
y_check = 3

  # Condições (pequisa):
  # 1. x é diferente de y (x != y)
  # 2. x é maior que zero (x > 0)
  # 3. y é maior que zero (y > 0)
  #  'and' garante que todas as condições sejam verdadeiras.

sao_diferentes_e_maiores_que_zero = (x_check != y_check) and (x_check > 0) and (y_check > 0)

print(f"Para x={x_check} e y={y_check}:")
print(f"São diferentes e maiores que zero? {sao_diferentes_e_maiores_que_zero}")
print("=" * 40)

# Questão 8
print("\n===> Questão 8")
result_1 = (5 > 3) 
result_2 = (2 < 1)
result = result_1 and result_2
print(f"O resultado da expressão '(5 > 3) and (2 < 1)' é: {result}")
print(f"Explicação: A primeira parte (5 > 3) é {result_1}. ")
print(f"A segunda parte (2 < 1) é {result_2}. ")
print("Como o operador 'and' exige que ambas as condições sejam Verdadeiras para que o resultado final seja Verdadeiro, e uma delas é Falsa, o resultado completo da expressão é Falso.")
print("=" * 40)

# Questão 9
print("===> Questão 9")
altura_str = "1.75"
altura_float = float(altura_str) # Converte a string para float

print(f"A altura convertida é: {altura_float}")
print(f"Confirmando o tipo: {type(altura_float)}") 
print("=" * 36)

# Questão 10
print("===> Questão 10")
alunos_python = {"Aluno1", "Aluno2", "Aluno3"}
alunos_java = {"Louco1", "Louco2", "Louco3"}

# a) Mostre os alunos que fazem as duas linguagens (interseção)
alunos_ambas = alunos_python & alunos_java
print(f"Alunos que fazem as duas linguagens: {alunos_ambas}")

# b) Mostre os alunos que fazem só Python (diferença)
alunos_so_python = alunos_python - alunos_java
print(f"Alunos que fazem só Python: {alunos_so_python}")

# c) Mostre todos os alunos (sem repetição) (união)
todos_alunos = alunos_python | alunos_java
print(f"Todos os alunos (sem repetição): {todos_alunos}")
print("=" * 95)

print("\n### Fim ###")
print("\nTodos os direitos reservados ao autor")
