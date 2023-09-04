# Pesquisa Binária
---

- Busca de um item de uma lista **ordenada**
- Em contraste com uma pesquisa simples(um por um), que pode exigir no pior caso n etapas para uma lista de n itens, já a pesquisa binária precisa de no máximo log₂(n) etapas.

## Exemplos e Comparações

### Pesquisa Simples

Usando pesquisa simples, você teria que verificar item por item, o que resultaria em **100 etapas** no pior caso.
100 -> 99 -> 98 -> 97 -> ...
### Pesquisa Binária

  
A pesquisa binária inicia no meio da lista e, com base nas verificações, elimina metade dos elementos a cada passo, o que significa que ela precisa de apenas log₂(n) etapas para encontrar o item desejado. Por exemplo, em uma lista de 100 itens:

1. Inicialmente, estamos no meio: 50.
2. Próxima verificação: 25.
3. Continuamos a reduzir pela metade até encontrar o item desejado.

100 itens: 50 -> 25 -> 13 -> 7 -> 4 -> 2 -> 1
log₂(100) ≈ 7
**7 etapas**

240.000 itens -> ...
log₂(240.000) ≈ 18 etapas
**18 etapas**