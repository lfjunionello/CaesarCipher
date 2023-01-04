import ply.lex as lex


tokens = [
   'EKEY',                  # Token para as chaves de encriptação
   'DKEY',                  # Token para as chaves de encriptação
   'SYMBOL',                # Token para os simbolos encontrados no texto
   'UPPERCASE',             # Token para as letras maiusculas encontradas no texto
   'LOWERCASE',             # Token para as letras minusculas encontradas no texto
   'NUMBER',                # Token para os numeros encontrados no texto
   'SPACE'                  # Token para os espacos encontrados no texto
]

# Expressões regulares simples
t_UPPERCASE    = r'[A-Z]+'
t_LOWERCASE = r'[a-z]+'
t_SYMBOL   = r'[-\+\*/\(\)\[\]\{\}\!\?\.\,\$\#\&\@\%\|\<\>\=\:\;\"\'\`\~\^\_\\]+'
t_SPACE = r'[\s]'

# Expressões regulares com ações
def t_NUMBER(t):
    r'\d+'
    t.value = t.value
    return t


#As chaves de encriptação seguem o modelo $E-<KEY>$ ou $D-<KEY>$
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


# Regra para contabilizar as linhas, para identificar erros
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caraacteres ignorados
t_ignore  = '\t'


# Função para tratar erros
def t_error(t):
    print(f'Illegal character "{t.value[0]}\n{t.lexer.__dict__}"')
    t.lexer.skip(1)

# Buildando o lex
lexer = lex.lex()