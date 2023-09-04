# Recursão e Pilhas
---

Como Leigh Caldwell, do Stacker Overflow, afirmou: "Os loops podem melhorar o desempenho do seu programa. A recursão melhora o desempenho do programador."
## Recursão

A recursão é uma técnica amplamente utilizada em algoritmos, embora nem sempre melhore o desempenho computacional, ela oferece uma maneira elegante de resolver problemas.

Recursão ocorre quando uma função chama a si mesma. Sua estrutura básica consiste em dois elementos:

- Caso Recursivo: Quando a função se chama novamente.
- Caso Base: Quando a função não se chama novamente, evitando um loop infinito.

Desvantagem: Consumo de memória. Cada chamada recursiva alocará mais espaço na pilha de chamadas para armazenar informações da função, mantendo das chamadas incompletas das anteriores.

Temas para estudar futuramente: 
- Recursão de cauda

## Pilhas

As pilhas são estruturas de dados simples que oferecem apenas duas operações fundamentais: **Push** (adicionar um item ao topo) e **Pop** (remover o item do topo).

Os computadores usam uma pilha interna, conhecida como "pilha de chamada", que é claramente observável nas chamadas de funções. Cada chamada de função adiciona um bloco de código ao topo da pilha, e quando a função é concluída, esse bloco é removido.

As pilhas de chamada são essenciais para o funcionamento da recursão e desempenham um papel crucial na execução de programas.