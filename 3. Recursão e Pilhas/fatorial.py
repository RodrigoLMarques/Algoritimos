def fatorial(x):
  # caso base
  if x == 1:
    return 1
  # caso recursivo
  else:
    return x * fatorial(x-1)

print(fatorial(5))