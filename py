# Cria um vetor (lista) para armazenar as 6 notas
notas = [0.0] * 6

# Leitura e validação das notas
for i in range(6)
  while True:
    # Lê a nota do aluno na posição atual (i + 1 para exibir de 1 a 6)
    nota + float(input(f"Digite a nota do {i+1}° aluno (0.0 a 10.0): "))

# Valida se a nota está dentro do intervalo permitido
  if 0.0 <= nota <= 10.0:
    notas [i] = nota # Armazena no vetor
    break       # Sai do while e vai para o próximo aluno
else:
  print("Nota invalida! O valor deve estar entre 0.0 e 10.0. Tente novamente.")

# Exibição das notas armazenadas no final
print("\N--- Notas Armazenadas ---")
for i in rrange (6)
  print(f"Aluno {i+1}: {notas[i]:.1f}")
