import re
import sys

# palavras reservadas
RESERVADAS = {'LIMIT'}

# especificacao dos tokens (a ordem importa: o primeiro padrao que encaixa ganha)
ESPECIFICACAO = [
    ('COMENTARIO', r'\#[^\n]*'),                      # # ate ao fim da linha (ignorado)
    ('STRING',     r'"[^"]*"'),                       # qualquer sequencia entre aspas
    ('VAR',        r'\?[A-Za-z0-9_]+'),               # ? seguido de alfanumericos
    ('LANG',       r'@[A-Za-z]{2}'),                  # @ seguido de 2 carateres
    ('NUM',        r'\d+'),                           # valor numerico
    ('ID',         r'[A-Za-z_][A-Za-z0-9_]*(?::[A-Za-z0-9_]+)?'),  # conceito (ex: a, dbo:artist)
    ('LCHAVETA',   r'\{'),                            # delimitadores
    ('RCHAVETA',   r'\}'),
    ('PONTO',      r'\.'),
    ('NEWLINE',    r'\n'),                            # para contar linhas
    ('SKIP',       r'[ \t\r]+'),                      # espaços (ignorados)
    ('ERRO',       r'.'),                             # qualquer outro caracter
]

REGEX = re.compile('|'.join(f'(?P<{nome}>{padrao})' for nome, padrao in ESPECIFICACAO))


def tokenize(texto):
    tokens = []
    linha = 1
    inicio_linha = 0

    for m in REGEX.finditer(texto):
        tipo = m.lastgroup
        valor = m.group()
        coluna = m.start() - inicio_linha + 1

        if tipo == 'NEWLINE':
            linha += 1
            inicio_linha = m.end()
            continue
        if tipo in ('SKIP', 'COMENTARIO'):
            continue
        if tipo == 'ID' and valor in RESERVADAS:
            tipo = valor                      # 'LIMIT' passa a ser token proprio
        elif tipo == 'NUM':
            valor = int(valor)
        elif tipo == 'ERRO':
            print(f'Erro léxico: caráter inesperado {valor!r} na linha {linha}, coluna {coluna}',
                  file=sys.stderr)

        tokens.append((tipo, valor, linha, coluna))

    return tokens


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding='utf-8') as f:
            texto = f.read()
    else:
        texto = sys.stdin.read()

    for tipo, valor, linha, coluna in tokenize(texto):
        print(f'{linha:>3}:{coluna:<3} {tipo:<10} {valor}')


if __name__ == '__main__':
    main()