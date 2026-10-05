## TPC2: Conversor de Markdown para HTML

## Autor 
- nome: João Paulo Pires Cascais
- id: a110393
- foto:
<img src="0155baed-793d-44a1-88e8-dfb3e4176d2f.jpg" width = "100">


## Resumo
Neste TPC fiz um pequeno conversor de Markdown para HTML em Python, que trata os elementos da "Basic Syntax" da Cheat Sheet: cabeçalhos, bold, itálico, listas numeradas, links e imagens.

Para isso usei o módulo re. O programa lê o ficheiro Markdown linha a linha e, para cada elemento, usa uma expressão regular que o encontra e o substitui pela tag de HTML correspondente.

alguns cuidados:

- O bold tem de ser tratado antes do itálico, senão os dois asteriscos do bold eram confundidos com os do itálico.
- A imagem tem de ser tratada antes do link, porque as duas têm o mesmo formato e a única diferença é o ponto de exclamação no início da imagem.
- Usei quantificadores não-gananciosos, como vimos na aula, para que duas palavras a negrito na mesma linha não fiquem juntas dentro da mesma tag.
- Nos cabeçalhos, conto o número de cardinais para saber se é h1, h2 ou h3.
- Nas listas numeradas, a lista é aberta quando aparece o primeiro item e fechada quando aparece uma linha que já não é item.


## Lista de Resultados

- [tpc2.py](tpc2.py): código do conversor
- [Exemplo.md](Exemplo.md): ficheiro de teste em Markdown
- [exemplo.html](exemplo.html): resultado da conversão do ficheiro de teste
