## TPC3: Analisador Léxico

## Autor 
- nome: João Paulo Pires Cascais
- id: a110393
- foto:
<img src="0155baed-793d-44a1-88e8-dfb3e4176d2f.jpg" width = "100">


## Resumo
- Neste trabalho foi construído, em Python, um analisador lexico para uma linguagem de query semelhante a SPARQL, como a usada para consultar a DBPedia.

- O analisador usa o módulo re e uma única expressão regular composta por grupos nomeados (um por tipo de token). A função tokenize percorre o texto com re.finditer e devolve uma lista de tuplos (tipo, valor, linha, coluna).

- Tokens reconhecidos:
  - COMENTARIO: começa em # e vai até ao fim da linha; é ignorado.
  - VAR: identificador de variável, ? seguido de carateres alfanuméricos (ex: ?nome).
  - LANG: identificador de língua, @ seguido de 2 carateres (ex: @en).
  - STRING: qualquer sequência entre aspas (ex: "Chuck Berry").
  - NUM: valor numérico (ex: 1000), convertido para inteiro.
  - ID: identificador de conceito, sequência de alfanuméricos com prefixo opcional (ex: a, select, dbo:artist).
  - LIMIT: palavra reservada, detetada como ID e depois reclassificada.
  - LCHAVETA, RCHAVETA, PONTO: os delimitadores ( { , } e . ).

- Espaços e mudanças de linha são ignorados, mas as mudanças de linha são contadas para indicar a posição de cada token. Qualquer caráter não reconhecido gera um token ERRO e uma mensagem no stderr.

- Utilização:
  python analisador_lexico.py exemplo.txt

## Lista de Resultados

- [analisador_lexico.py](analisador_lexico.py): código do analisador léxico
- [exemplo.txt](exemplo.txt): query de exemplo do enunciado
- [output.txt](output.txt): lista de tokens produzida para o exemplo
