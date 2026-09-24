## TPC1: Expressão regular para strings binárias sem a substring "011" 

## Autor 
- nome: João Paulo Pires Cascais
- id: a110393
- foto: <img src="0155baed-793d-44a1-88e8-dfb3e4176d2f.jpeg" width = "200">


## Resumo

Este trabalho apresenta uma expressão regular que reconhece todas as strings binárias (alfabeto {0, 1}) que não contêm a substring 011. A solução obtida é 1*(0|01)*.

Antes do primeiro 0 pode aparecer qualquer número de 1s, porque o padrão 011 exige um 0 antes dos dois 1s. Essa parte corresponde a 1*.

Depois do primeiro 0, não podem aparecer dois 1s seguidos, caso contrário formar-se-ia 011. Assim, cada 1 surge imediatamente a seguir a um 0, e o resto da string é uma sequência de blocos 0 ou 01. Essa parte corresponde a (0|01)*.

## Resultado 
[Resultado](resultado.md)


