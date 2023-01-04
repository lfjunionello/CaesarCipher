from tkinter import E
import ply.yacc as yacc

from lex import tokens


''' 
<<GRAMATICA>>

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
'''
def encryptStr(text, key):
    result = ''
    for i in text :
        temp = ''
        """ print(i) """

        if(i[1] == "symbol"):
            for j in i[0]:
                result += j
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
    return result


def decryptStr(text, key):
    return encryptStr(text, -key) 



def p_file(p):
    'file : content'
    p[0] = p[1]

def p_content_d(p):
    'content : EKEY decrypted'
    p[0] = encryptStr(p[2], p[1])

def p_content_e(p):
    'content : DKEY encrypted'
    p[0] = decryptStr(p[2], p[1])


#Encriptado/decriptado
def p_decrypted_text(p):
    'decrypted : text'
    p[0] = p[1]

def p_encrypted(p):
    'encrypted : text'
    p[0] = p[1]


# Texto
def p_text_1(p):
    'text : text element'
    p[0] = p[1] + [p[2]]

def p_text_2(p):
    'text : element'
    p[0] = [p[1]]



# Elementos
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



def p_error(p):
    print(f"Syntax error in input!")

# Buildando o parser
parser = yacc.yacc()