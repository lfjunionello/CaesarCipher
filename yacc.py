from tkinter import E
import ply.yacc as yacc

# NECESSARIOS IMPORTAR OS TOKENS DO LEX
from lex import tokens


''' GRAMATICA

file -> content

content -> EKEY decrypted
content -> DKEY encrypted

decrypted -> text
encrypted -> text

text -> text element
text -> element

element -> UPPERCASE
element -> LOWERCASE
element -> NUMBER
element -> SYMBOL
element -> SPACE

---- ACERTAR ESSA PARTE AQUI




'''
def encryptStr(text, key):
    result = ''
    for i in text :
        temp = ''
        """ print(i) """

        if(i[1] == "symbol"):
            for j in i[0]:
                result += i[0]
            continue

        elif(i[1] == "upper"):
            for j in i[0]:
                unicodeID = ord(j)
                unicodeID += key
                if(unicodeID > 90):
                    unicodeID -= 26
                elif(unicodeID < 65):
                    unicodeID += 26
                result += chr(unicodeID)
            continue

        elif(i[1] == "lower"):
            for j in i[0]:
                unicodeID = ord(j)
                unicodeID += key
                if(unicodeID > 122):
                    unicodeID -= 26
                elif(unicodeID < 97):
                    unicodeID += 26
                result += chr(unicodeID)
            continue

        elif(i[1] == "number"):
            for j in i[0]:
                unicodeID = ord(j)
                unicodeID += key
                if(unicodeID > 57):
                    unicodeID -= 10
                elif(unicodeID < 48):
                    unicodeID += 10
                result += chr(unicodeID)
            continue


        """ unicodeID = ord(i[0])
        temp += chr(unicodeID+key) 
        type = i[1][0].upper()   # PEGAR O PRIMEIRO CARACTERE DO TIPO
        result += f'{type}<{temp}>' """
    return result

def generate_key(letter):
    dic = {'C': 'consonant', 'N': 'number', 'V': 'vogal', 'S': 'symbol'}
    return dic[letter] + '_k'

def decryptStr(text, key):
    encryptStr(text, -key)
    """ result = ''
    for i in text :
        temp = ''
        key_parsed = generate_key(i['type'])
        for j in i['content']:
            unicodeID = ord(j)
            temp += chr(unicodeID-key[key_parsed])
            if temp == "_": 
                temp = " "
        result += temp """
    return encryptStr(text, -key) 

# ARQUIVOS SÃO CONJUNTOS DE CONTEÚDOS 



def p_file(p):
    'file : content'
    p[0] = p[1]



# CONTEUDOS SAO GERADOS DE UMA CHAVE E UM TEXTO DECRIPTADO OU ENCRIPTADO

def p_content_d(p):
    'content : EKEY decrypted'
    p[0] = encryptStr(p[2], p[1])

def p_content_e(p):
    'content : DKEY encrypted'
    p[0] = decryptStr(p[2], p[1])



# TEXTOS DECRIPTADOS

def p_decrypted_text(p):
    'decrypted : text'
    p[0] = p[1]



# TEXTOS ENCRIPTADOS

def p_encrypted(p):
    'encrypted : text'
    p[0] = p[1]

""" def p_encrypted_object(p):
    'encrypted : object'
    p[0] = [p[1]] """
    


# OBJETOS SAO PASSADOS COMO FORAM RECONHECIDOS
""" 
def p_object(p):
    'object : EOBJECT'
    p[0] = p[1] """



# PALAVRAS SAO PASSADAS COMO LISTAS PARA ENCRIPTACAO

def p_text_1(p):
    'text : text element'
    p[0] = p[1] + [p[2]]

def p_text_2(p):
    'text : element'
    p[0] = [p[1]]



# ELEMENTOS SÃO IDENTIFICADOS COM SEUS RESPECTIVOS TIPOS PARA A ENCRIPTACAO 


def p_element_uppercase(p):
    'element : UPPERCASE'
    p[0] = (p[1],'upper')

def p_element_lowercase(p):
    'element : LOWERCASE'
    p[0] = (p[1], 'lower')

def p_element_number(p):
    'element : NUMBER'
    p[0] = (p[1], 'number')

def p_element_symbol(p):
    'element : SYMBOL'
    p[0] = (p[1], 'symbol')

def p_element_space(p):
    'element : SPACE'
    p[0] = (' ', 'symbol')


# FUNÇÃO PARA LIDAR COM ERROS
def p_error(p):
    print(f"Syntax error in input!")

# BUILD DO PARSER
parser = yacc.yacc()