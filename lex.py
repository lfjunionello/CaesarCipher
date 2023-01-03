import ply.lex as lex

# LISTA COM NOMES DOS TOKENS
tokens = [
   'EKEY',                  # Token para as chaves de encriptação
   'DKEY',                  # Token para as chaves de encriptação
   'SYMBOL',                # Token para os simbolos encontrados no texto
   'UPPERCASE',             # Token para as letras maiusculas encontradas no texto
   'LOWERCASE',             # Token para as letras minusculas encontradas no texto
   'NUMBER',                # Token para os numeros encontrados no texto
   'SPACE'                  # Token para os espacos encontrados no texto
]

# EXPRESSÕES REGULARES SIMPLES
t_VOGAL    = r'[aeiouáàâãéèêíïóôõöúAEIOUÁÀÂÃÉÈÍÏÓÔÕÖÚ]+'
t_CONSONANT = r'[b-df-hj-np-tv-zçñ|B-DF-HJ-NP-TV-ZÇÑ]+'
t_SYMBOL   = r'[-\+\*/\(\)\[\]\{\}\!\?\.\,\$\#\&\@\%\|\<\>\=\:\;\"\'\`\~\^\_\\]+'
t_SPACE = r'[\s]'

# EXPRESSÕES REGULARES QUE PRECISAM DE UMA AÇÃO
def t_NUMBER(t):
    r'\d+'
    t.value = t.value
    return t

'''AS CHAVES DE ENCRIPTACAO E DECRIPTACAO SEGUEM O MODELO

        $TYPE-CKEY-VKEY-NKEY-SKEY$

    - Type -> tipo de chave [E, D] 
    - CKey -> chave para as consoantes  [números de 0-29]
    - VKey -> chave para as vogais      [números de 0-29]
    - NKey -> chave para as numeros     [números de 0-29]
    - SKey -> chave para as simbolos    [números de 0-29]
'''

def t_EKEY(t):
    r'\$E-([1-9]|[1][0-9]|[2][0-5])\$'
    _, key = t.value.replace('$', '').split('-') 
    t.value = int(key)
    return t

def t_DKEY(t):
    r'\$D-([1-9]|[1][0-9]|[2][0-5])\$'
    _, key = t.value.replace('$', '').split('-') 
    t.value = int(key)
    return t

'''OS OBJETOS DE ENCRIPTACAO SEGUEM O MODELO

        TYPE<TEXTO>

    - Type: tipo do objeto [C, V, N, S]
    - Texto: grupo de caracteres encriptados
'''

# REGRA CRIADA PARA CONTAR A QUANTIDADE LINHAS (SUGERIDO PELO LEX PARA FACILITAR ENCONTRAR O ERRO)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# CARACTERES IGNORADOS PELO ANALISADOR
t_ignore  = '\t'


# FUNÇÃO DE ERRO CASO O ANALISADOR NAO IDENTIFIQUE O TOKEN
def t_error(t):
    print(f'Illegal character "{t.value[0]}\n{t.lexer.__dict__}"')
    t.lexer.skip(1)

# BUILD DO LEX
lexer = lex.lex()